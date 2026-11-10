from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserCreateSerializer


class UserRegistrationAPIView(APIView):
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

    def post(self, request, *args, **kwargs):
        return Response({"message": "Handling a POST request!"})


class UserLoginAPIView:
    """
    success response format
     {
       auth_token: ""
     }
    """
