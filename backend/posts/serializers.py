from taggit.serializers import TaggitSerializer, TagListSerializerField

from rest_framework import serializers
from .models import Post

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