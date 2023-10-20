from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Q

from posts.models import Post
from accounts.models import Profile

"""
Search View
"""

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def search(request, search_content):
    posts_data = []
    profiles_data = []
    posts = Post.objects.filter(
        Q(tags__name__icontains=search_content) | 
        Q(title__icontains=search_content) | 
        Q(description__icontains=search_content)
    ).distinct()
    profiles = Profile.objects.filter(
        Q(username_profile__icontains=search_content)
    ).distinct()
    for post in posts:
        post_info = {
            'id': post.pk,
            'title': post.title,
            'description': post.description,
            'tags': [tag.name for tag in post.tags.all()],
            'creator': post.user_creator.username_profile
        }
        posts_data.append(post_info)
    for profile in profiles:
        profile_info = {
            'id': profile.pk,
            'username': profile.username_profile
        }
        profiles_data.append(profile_info)
    return Response({'Posts': posts_data, 'Profiles': profiles_data}, status=status.HTTP_200_OK)