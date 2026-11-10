from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


# Add your serializers
class UserSerializerWithoutIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email"]


class UserSerializerWithIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "first_name", "last_name", "email"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["name", "first_name", "last_name", "email", "date_joined", "token"]
        read_only_fields = ["date_joined", "token"]
