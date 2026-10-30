from django.urls import path
from todos.views import TodoAPIViewSet

app_name = 'todos'

from rest_framework import routers


router = routers.SimpleRouter()


router.register(r'todos', TodoAPIViewSet, 'todos')

urlpatterns = router.urls
