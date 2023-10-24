from django.test import TestCase
from django.contrib.auth.models import User

from accounts.models import Profile
from .models import Post
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
            'title': 'Test title serializer',
            'description': 'Test description serializer',
            'tags': ['Test Serializer', 'Test'],
            'profile_creator': self.profile.pk
        }

    def test_create_post_serializer(self):
        """
        This test checks if the serializer works to create a `Post`.
        """
        serializer_post = PostSerializer(data=self.data)
        serializer_post.is_valid()
        post_created = serializer_post.save()
        self.assertEqual(post_created.title, self.data['title'])
        self.assertEqual(post_created.description, self.data['description'])
        self.assertEqual(post_created.tags, self.data['tags'])
        self.assertEqual(post_created.profile_creator.id, self.data['profile_creator'])


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
        self.post = Post.objects.create(
            title='Title test posts',
            description='Description test',
            tags='Test',
            profile_creator=self.profile
        )
        self.comment = {
            'body': 'Esto es un test de body de comentario',
            'post': self.post.pk,
            'profile_comment_creator': self.profile.pk
        }

    def test_create_comment_serializer(self):
        serializer_comment = CommentSerializer(data=self.comment)
        serializer_comment.is_valid()
        comment_created = serializer_comment.save()
        self.assertEqual(comment_created.body, self.comment['body'])
        self.assertEqual(comment_created.post.id, self.comment['post'])
        self.assertEqual(comment_created.profile_comment_creator.id, self.comment['profile_comment_creator'])