from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Todo
from .serializers import TodoCreateSerializer, TodoUpdateSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"
    max_page_size = 100


class TodoAPIViewSet(ModelViewSet):
    """
    success response for create/update/get
    {
      "name": "",
      "done": true/false,
      "date_created": ""
    }

    success response for list
    [
      {
        "name": "",
        "done": true/false,
        "date_created": ""
      }
    ]
    """

    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        self.queryset = Todo.objects.all().order_by("id")
        user_id = self.request.query_params.get("user_id")
        if user_id:
            self.queryset = Todo.objects.filter(user_id=user_id).order_by("id")
        return self.queryset

    def get_serializer_class(self):
        if self.action == "create":
            return TodoCreateSerializer
        return TodoUpdateSerializer
