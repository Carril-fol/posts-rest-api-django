from .serializers import PostSerializer
from .models import Post

from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


# Create your views here.
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

#Agregar funciones:

    # Comentarios:
        # Crear Comentarios en un `Post` especifico
        # Si el creador quiere poder borrarlos o editarlo de un `Post` especifico

    # Likes:
        # Poder likear `Posts`
        # Poder likear `Comentarios`
        # Deslikear `Posts` y `Comentarios`