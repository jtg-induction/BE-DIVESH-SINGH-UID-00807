from django.urls import path
from users.views import UserRegistrationAPIView, UserLoginAPIView

app_name = "users"

urlpatterns = [
    path("", UserRegistrationAPIView.as_view(), name="register"),
    path("login/", UserLoginAPIView.as_view(), name="login"),
]
