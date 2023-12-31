# Generated by Django 4.2.6 on 2023-10-19 17:03

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_profile', models.CharField(blank=True, max_length=50, null=True)),
                ('genders', models.CharField(choices=[('He/Him', 'He/Him'), ('She/Her', 'She/Her'), ('I prefer not to say', 'I prefer not to say'), ('Personalized', 'Personalized')], max_length=20)),
                ('custom_genre', models.CharField(blank=True, max_length=30, null=True)),
                ('description_profile', models.TextField(blank=True, null=True)),
                ('img_profile', models.ImageField(blank=True, null=True, upload_to=accounts.models.profile_pictures_per_user_directory)),
                ('followers', models.ManyToManyField(related_name='followers_profiles', to=settings.AUTH_USER_MODEL)),
                ('follows', models.ManyToManyField(related_name='follows_profiles', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
