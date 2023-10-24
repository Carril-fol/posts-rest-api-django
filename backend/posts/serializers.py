from taggit.serializers import TaggitSerializer, TagListSerializerField

from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'tags', 'profile_creator']

    def create(self, validated_data):
        post_data = Post.objects.create(**validated_data)
        return post_data
    

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'post', 'body', 'profile_comment_creator', 'created_date_comment']

    def create(self, validated_data):
        comment_data = Comment.objects.create(**validated_data)
        return comment_data