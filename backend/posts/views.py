from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment

from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


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
        return Response({"title": user_post.title, "description": user_post.description}, status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, post_id):
    user_post = get_object_or_404(Post, id=post_id)
    user_post.delete()  
    return Response({'message':'Post deleted'}, status=status.HTTP_200_OK)


"""
Comment Views
"""

@api_view(['POST'])
@permission_classes([IsAuthenticated]) # Funciona
def create_comment(request, post_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Comment created'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_comment(request, comment_id): # Funciona
    comment_user_posted = get_object_or_404(Comment, id=comment_id)
    serializer = CommentSerializer(instance=comment_user_posted, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Comment updated'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Comentarios:
    # Funcion que permita borrar un comentario especifico

# Likes:
    # Poder likear `Posts`
    # Poder likear `Comentarios`
    # Deslikear `Posts` y `Comentarios`