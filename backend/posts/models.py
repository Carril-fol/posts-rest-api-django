from django.db import models

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from bs4 import BeautifulSoup

from accounts.models import Profile

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=280, null=False, blank=False)
    description = RichTextField(null=True, blank=True)
    tags = TaggableManager()
    likes = models.ManyToManyField(Profile, related_name='likes')
    profile_creator = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=False)

    def likes_posts_count(self):
        likes_count = self.likes.count()
        return likes_count
    
    def __str__(self):
        tags_formatted = ", ".join(self.tags.names())
        soup = BeautifulSoup(self.description, 'html.parser')
        images = soup.find_all('img')
        cleaned_description_image = ' '.join(soup.stripped_strings)
        cleaned_description_not_image_in = ' '.join(soup.stripped_strings)
        result_images = f'Title: {self.title} / Description: {cleaned_description_image}'
        result_without_images = f'Title: {self.title} / Description: {cleaned_description_not_image_in} / Tags: {tags_formatted} / Creator: {self.user_creator.username_profile}'
        for image in images:
            result_images += f' <img src="{image["src"]}"> / Tags: {tags_formatted} / Creator: {self.user_creator.username_profile}'
        if images:
            return result_images
        else:
            return result_without_images


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = RichTextField()
    created_date_comment = models.DateField(auto_now=True, null=False, blank=False)
    likes_comment = models.ManyToManyField(Profile, related_name='post_comment_likes')
    profile_comment_creator = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def likes_blog_count(self):
        return self.likes_comment.count()
    
    def __str__(self) -> str:
        result = f'User creator: {self.user_creator_comment} \ Body: {self.body}'
        return result