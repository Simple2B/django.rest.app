from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')


class RegisterUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password')

    def validate_password(self, value: str) -> str:    
        """    
            Hash value passed by user.    
            :param value: password of a user    
            :return: a hashed version of the password
        """    
        return make_password(value)
