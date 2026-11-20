from django.urls import path
from .views import ProjectMemberApiViewSet

urlpatterns = [path("", ProjectMemberApiViewSet.as_view())]
