from rest_framework.test import APITestCase
from rest_framework import status

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

#Agregar tests