from rest_framework import serializers
from .models import RegisterUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = RegisterUser
        fields = ('name', 'email', 'password')
    def create(self,validated_data):
        user = RegisterUser.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255, write_only=True)

