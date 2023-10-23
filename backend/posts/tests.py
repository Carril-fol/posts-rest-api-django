from rest_framework.test import APITestCase, APIRequestFactory

from django.test import TestCase
from django.contrib.auth.models import User

from accounts.models import Profile
from .serializers import PostSerializer, CommentSerializer

"""
Test Serializers
"""

class PostSerializerTest(TestCase):

    def setUp(self):
        """
        Values to be used in the tests
        """
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            user=self.user
        )
        self.data = {
            'id': 1,
            'title': 'Test title serializer',
            'description': 'Test description serializer',
            'tags': ['Test Serializer', 'Test'],
            'user_creator': self.profile.pk
        }

    def test_create_post(self):
        """
        This test checks if the serializer works to create a `Post`.
        """
        factory = APIRequestFactory()
        request = factory.post('api/builder-post/')
        request.user = self.profile
        serializer = PostSerializer(data=self.data, context={'request': request})
        
        serializer.is_valid()
        post = serializer.save()
        self.assertEqual(post.title, self.data['title'])
        self.assertEqual(post.description, self.data['description'])
        self.assertEqual(post.tags ,self.data['tags'])
        self.assertEqual(post.profile_creator, self.profile)


class CommentSerializerTest(TestCase):

    def setUp(self):
        """
        Values to be used in the tests
        """
        self.user = User.objects.create(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            user=self.user
        )
        self.post = {
            'id': 1,
            'title': 'Test title serializer',
            'description': 'Test description serializer',
            'tags': ['Test Serializer', 'Test'],
            'user_creator': self.profile.pk
        }
        self.comment = {
            'id': 1,
            'body': 'Esto es un test de body de comentario',
            'post': self.post['id'],
            'profile_comment_creator': self.profile.pk
        }

    def test_create_comment(self):
        """
        This test tests if the serializer works to create a comment in a post.
        """
        factory = APIRequestFactory()

        request_post = factory.post('api/builder-post/')
        request_post.user = self.profile
        serializer_post = PostSerializer(data=self.post, context={'request': request_post})

        if serializer_post.is_valid():
            post = serializer_post.save()
        else:
            print(serializer_post.errors)

        request_comment = factory.post('api/builder-comment/{}/'.format(post.id))
        request_comment.user = self.profile
        serializer_comment = CommentSerializer(data=self.comment, context={'request': request_comment})

        serializer_comment.is_valid()
        comment = serializer_comment.save()
        self.assertEqual(comment.body, self.comment['body'])
        self.assertEqual(comment.profile_comment_creator, self.profile)