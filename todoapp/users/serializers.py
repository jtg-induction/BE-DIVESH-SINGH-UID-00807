from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import  ValidationError 
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .constants import PASSWORD_MISMATCH

User = get_user_model()


class UserSerializerWithIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]


class UserSerializerWithoutIdSerializer(UserSerializerWithIdSerializer):
    class Meta:
        model = User
        fields = [fields for fields in UserSerializerWithIdSerializer.Meta.fields if fields !='id']
        

class UserCreateSerializer(UserSerializerWithoutIdSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = UserSerializerWithoutIdSerializer.Meta.fields+[
            "password",
            "confirm_password",
            "date_joined",
            "token",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def get_token(self, obj):
        token = Token.objects.filter(user=obj).first()
        return token.key if token else None
    
    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(list(e.messages))
        return value
    
    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": PASSWORD_MISMATCH})
        return attrs

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop("password")
        validated_data.pop("confirm_password")
        User = get_user_model().objects.create_user(
            email=email, password=password, **validated_data
        )
        Token.objects.get_or_create(user=User)
        return User


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
