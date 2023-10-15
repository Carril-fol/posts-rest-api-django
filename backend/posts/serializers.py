from taggit.serializers import TaggitSerializer, TagListSerializerField

from rest_framework import serializers
from django.utils import timezone
from .models import Post, Comment

#Crear serializers
class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'tags', 'user_creator']

    def create(self, validated_data):
        user_creator = self.context['request'].user
        post_data = Post.objects.create(**validated_data, user_creator=user_creator)
        return post_data
    

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['post', 'body', 'user_creator_comment']
        read_only = ['id', 'post', 'created_date_comment']

    def create(self, validated_data):
        """
        """
        user_creator = self.context['request'].user
        created_date = timezone.now()
        comment_data = Comment.objects.create(**validated_data, created_date_comment=created_date, user_creator_comment=user_creator)
        return comment_data