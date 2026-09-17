from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "user",
            "profile_username",
            "is_active",
            "bio",
            "profile_picture",
        ]

    user = UserSerializer()
    profile_username = serializers.CharField(source="username")
