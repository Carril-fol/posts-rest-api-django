from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, api_view

from django.shortcuts import get_object_or_404

from .serializers import RegisterSerializer, ProfileSerializer
from .models import Profile

# Create your views here.
"""
Accounts Views
"""

class RegisterView(APIView):

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_pair_view = TokenObtainPairView.as_view()
            token_request = request._request
            token_request.data = {
                'username': user.username,
                'password': request.data.get('password')
            }
            response = token_pair_view(token_request)
            return response
        else:
            return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
    

class LogoutView(APIView):
    authentication_classes = (JWTAuthentication,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successful logout'}, status=status.HTTP_200_OK)
        except TokenError as error_token:
            return Response({'message': 'Invalid refresh token', 'error': str(error_token)}, status=status.HTTP_400_BAD_REQUEST)
        
"""
Profile Views
"""

class ProfileUpdate(APIView):
    authentication_classes = (JWTAuthentication,)

    def update(self, request, profile_id):
        profile_user = get_object_or_404(Profile, id=profile_id)
        serializer = ProfileSerializer(instance=profile_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Profile update'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetail(APIView):
    authentication_classes = (JWTAuthentication,)

    def get(self, request, profile_user_id):
        try:
            profile_user = get_object_or_404(Profile, id=profile_user_id)
            following_profiles = profile_user.followers.count()
            follows_profile = profile_user.follows.count()
            profile_data = {
                'username_profile': profile_user.username_profile,
                'description': profile_user.description_profile,
                'following_count': following_profiles,
                'follows': follows_profile,
                'genders': profile_user.genders,
                'custom_gender': profile_user.custom_genre
            }
            return Response({'Profile data': profile_data}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({'message': 'Profile Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def follow_profile(request, profile_id):
    follow = False
    profile = get_object_or_404(Profile, id=profile_id)
    user = request.user
    if user in profile.followers.all():
        profile.followers.remove(user)
        follow = False
        message = 'Unfollow'
    else:
        profile.followers.add(user)
        follow = True
        message = 'Follow'
    return Response({'message': message}, status=status.HTTP_200_OK)