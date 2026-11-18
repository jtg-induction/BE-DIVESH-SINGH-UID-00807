from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

User = get_user_model()


class UserSerializerWithIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]


class UserSerializerWithoutIdSerializer(UserSerializerWithIdSerializer):
    class Meta:
        model = User
        fields = [fields for fields in UserSerializerWithIdSerializer.Meta.fields if fields !='id']
