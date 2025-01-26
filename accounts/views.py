from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from .serializers import UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


# Creating JWT tokens manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return str(refresh.access_token)


class UserLoginView(APIView):
    permission_classes = [AllowAny]
    access_token = None
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)

            # Return a token for authentication
            token = get_tokens_for_user(user=user)

            return Response({
                'token': token,
                'user_id': user.pk,
                'username': user.username
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
