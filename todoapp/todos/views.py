from rest_framework.viewsets import ModelViewSet
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
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        self.queryset = Todo.objects.filter(user_id=self.request.user.id).order_by("id")
        return self.queryset

    def get_serializer_class(self):
        if self.action == "create":
            return TodoCreateSerializer
        return TodoUpdateSerializer
