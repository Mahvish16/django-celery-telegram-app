from django.shortcuts import render
from .models import RegisterUser,EmailVerification
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response;
from rest_framework import status;
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.conf import settings
import uuid
from .tasks import SendEmail

# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_active=False)
            SendEmail.delay(user.id)
            return Response({"message": "User created successfully, Please Verify your email"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)})
        else:
            return Response({"message": "Invalid email or Password"}, status= status.HTTP_404_NOT_FOUND)


class PublicView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello, this is a Public endpoint"}, status=status.HTTP_200_OK)

class ProtectView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return Response({"message": "Hello, this is a Protected endpoint"}, status=status.HTTP_200_OK)

class EmailVerificationView(generics.GenericAPIView):
    def get(self, request, token, *args, **kwargs):
        try:
            verification = EmailVerification.objects.get(token=token)
            user = verification.user
            user.is_active = True
            user.save()
            verification.delete()
            return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
        except EmailVerification.DoesNotExist:
            return Response({"error": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)

