from rest_framework.decorators import permission_classes, api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

"""
Posts Views
"""

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_post(request, post_id):
    user_post = get_object_or_404(Post, id=post_id)
    serializer = PostSerializer(instance=user_post, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Post updated successfully'}, status=status.HTTP_200_OK)
    return ResourceWarning(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_post(request, post_id):
    try:
        user_post = get_object_or_404(Post, id=post_id)
        return Response({"id":user_post.pk, "title": user_post.title, "description": user_post.description, "likes": user_post.likes}, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):
    user_post = get_object_or_404(Post, id=post_id)
    user_post.delete()  
    return Response({'message':'Post deleted'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detail_post(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        comments= Comment.objects.filter(post=post)
        user_data = {
            'id' : post.user_creator.pk,
            'username': post.user_creator.username,
        }
        likes_post = {
            'count': post.likes.count()
        }
        commnets_data = []
        for comment in comments:
            comment_user_data = {
                'id': comment.user_creator_comment.pk,
                'username': comment.user_creator_comment.username,
            }
            comment_info = {
                'body': comment.body,
                'user_creator': comment_user_data,
            }
            commnets_data.append(comment_info)
        return Response({
            'Post': post.pk, 
            'Title': post.title, 
            'Description': post.description, 
            'User Creator': user_data, 
            'Likes': likes_post, 
            'Comments': commnets_data,
        }, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

"""
Comment Views
"""

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, post_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Comment created'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_comment(request, comment_id):
    comment_user_posted = get_object_or_404(Comment, id=comment_id)
    serializer = CommentSerializer(instance=comment_user_posted, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Comment updated'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request, comment_id):
    try:
        comment_user_posted = get_object_or_404(Comment, id=comment_id)
        comment_user_posted.delete()
        return Response({'message':'Comment deleted'}, status=status.HTTP_200_OK)
    except Comment.DoesNotExist:
        return Response({'message':'The comment does not exist'}, status=status.HTTP_400_BAD_REQUEST)

"""
Likes Views
"""

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_posts(request, post_id, user_id):
    liked = False
    get_id_user = get_object_or_404(User, id=user_id)
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=get_id_user.pk).exists():
        post.likes.remove(get_id_user.pk)
        liked = False
        message = 'Post unliked'
    else:
        post.likes.add(get_id_user.pk)
        liked = True
        message = 'Post liked'
    return Response({
        'message':message, 
        'Post': post.pk, 
        'Title': post.title, 
        'Description': post.description
        }, status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_id, user_id):
    liked = False
    get_id_user = get_object_or_404(User, id=user_id)
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.likes_comment.filter(id=get_id_user.pk).exists():
        comment.likes_comment.remove(get_id_user.pk)
        liked = False
        message = 'Comment unliked'
    else:
        comment.likes_comment.add(get_id_user.pk)
        liked = True
        message = 'Comment liked'
    return Response({
        'message':message, 
        'Comment': comment.pk, 
        'Body': comment.body, 
        'User Creator': comment.user_creator_comment.pk
        }, status=status.HTTP_200_OK)