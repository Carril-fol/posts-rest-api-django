from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=280, null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name='likes')
    user_creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)

    def likes_posts_count(self):
        return self.likes.count()
    
    def __str__(self):
        if len(self.description) > 150:
            description_acorted = self.description[::100] + '...'
            return f'Title: {self.title} / Description: {description_acorted} / Tags: {self.tags} / User: {self.user_creator}'
        else:
            return f'Title: {self.title} / Tags: {self.tags}'
        

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = RichTextField()
    created_date_comment = models.DateField(auto_now=True, null=False, blank=False)
    likes_comment = models.ManyToManyField(User, related_name='post_comment_likes')
    user_creator_comment = models.ForeignKey(User, on_delete=models.CASCADE)

    def likes_blog_count(self):
        return self.likes_comment.count()