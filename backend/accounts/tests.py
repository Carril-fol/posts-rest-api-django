from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile
from .serializers import ProfileSerializer, RegisterSerializer

"""
Test Serializers
"""

class RegisterSerializerTest(TestCase):

    def setUp(self):
        """
        Values to be used in the tests
        """
        self.data_user = {
            'username': 'Testusername',
            'first_name': 'Test First Name',
            'last_name': 'Test Last Name',
            'email': 'test@gmail.com',
            'password': 'testpassword123',
            'password2': 'testpassword123'
        }

    def test_create_user(self):
        serializer = RegisterSerializer(data=self.data_user)
        serializer.is_valid()
        user_created = serializer.save()
        self.assertEqual(user_created.username, self.data_user['username']),
        self.assertEqual(user_created.first_name, self.data_user['first_name']),
        self.assertEqual(user_created.last_name, self.data_user['last_name']),
        self.assertEqual(user_created.email, self.data_user['email'])


class ProfileSerializerTest(TestCase):

    def setUp(self):
        """
        Values to be used in the tests
        """
        self.create_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.profile = Profile.objects.create(
            user=self.create_user
        )
        self.data_profile_to_update = {
            'username_profile': 'Test Username Profile Update',
            'genders': 'He/Him',
            'custom_genre' : None,
            'description_profile': 'Test description Update'
        }
        self.data_user = {
            'username': 'Testusername',
            'first_name': 'Test First Name',
            'last_name': 'Test Last Name',
            'email': 'test@gmail.com',
            'password': 'testpassword123',
            'password2': 'testpassword123'
        }

    def test_create_profile(self):
        serializer_user = RegisterSerializer(data=self.data_user)
        serializer_user.is_valid()
        user_created_with_profile = serializer_user.save()
        user_instance = get_object_or_404(User, id=user_created_with_profile.id)
        profile_instance = get_object_or_404(Profile, id=user_created_with_profile.id)
        self.assertEqual(user_instance.username, self.data_user['username'])
        self.assertEqual(profile_instance.username_profile, user_instance.username)

    def test_update_profile(self):
        profile_instance = get_object_or_404(Profile, id=self.profile.pk)
        serializer_profile = ProfileSerializer(instance=profile_instance, data=self.data_profile_to_update)
        serializer_profile.is_valid()
        profile_updated = serializer_profile.save()
        self.assertEqual(profile_updated.username_profile, self.data_profile_to_update['username_profile'])
        self.assertEqual(profile_updated.genders, self.data_profile_to_update['genders'])
        self.assertEqual(profile_updated.custom_genre, self.data_profile_to_update['custom_genre'])
        self.assertEqual(profile_updated.description_profile, self.data_profile_to_update['description_profile'])