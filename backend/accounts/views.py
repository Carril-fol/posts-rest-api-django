from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .serializers import RegisterSerializer

# Create your views here.
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
    
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Successful logout'}, status=status.HTTP_200_OK)
        except TokenError as e:
            return Response({'message': 'Invalid refresh token', 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

#Agregar funciones:

    # Reseteo de contraseña por mail