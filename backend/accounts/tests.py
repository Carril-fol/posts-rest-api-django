from rest_framework.test import APITestCase, APIRequestFactory

from django.test import TestCase
from django.contrib.auth.models import User

from accounts.models import Profile
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