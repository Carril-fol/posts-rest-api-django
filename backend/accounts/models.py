from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def profile_pictures_per_user_directory(instance, filename):
    return 'media/images/profiles/user_{0}/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    username_profile = models.CharField(max_length=50, null=True, blank=True)
    GENDER_CHOICES = (
        ('He/Him', 'He/Him'),
        ('She/Her', 'She/Her'),
        ('I prefer not to say', 'I prefer not to say'),
        ('Personalized', 'Personalized')
    )
    genders = models.CharField(max_length=20, choices=GENDER_CHOICES)
    custom_genre = models.CharField(max_length=30, null=True, blank=True)
    description_profile = models.TextField(null=True, blank=True)
    img_profile = models.ImageField(upload_to=profile_pictures_per_user_directory, null=True, blank=True)
    followers = models.ManyToManyField(User, related_name='followers_profiles')
    follows = models.ManyToManyField(User, related_name='follows_profiles')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.img_profile:
            self.img_profile = 'profiles/default/image_default_profile.png'
        if not self.username_profile:
            self.username_profile = self.user.username
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f'Profile: {self.username_profile} \ Id: {self.user.pk}'