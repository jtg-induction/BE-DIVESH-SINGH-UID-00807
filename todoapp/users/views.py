from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .serializers import UserCreateSerializer, UserLoginSerializer

User=get_user_model()

class UserRegistrationAPIView(generics.GenericAPIView, mixins.CreateModelMixin):
    """
    success response format
     {
       first_name: "",
       last_name: "",
       email: "",
       date_joined: "",
       "token"
     }
    """

    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

    def post(self, request):
        return self.create(request)


class UserLoginAPIView(APIView):
    """
    success response format
     {
       auth_token: ""
     }
    """

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = (
                User
                .objects.filter(email=serializer.validated_data["email"])
                .first()
            )
            if user is not None and user.check_password(
                serializer.validated_data["password"]
            ):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"auth_token": token.key}, status=status.HTTP_200_OK)
            return Response(
                {"error": "Invalid email or password"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
