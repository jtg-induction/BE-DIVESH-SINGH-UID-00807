from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .pagination import StandardResultsSetPagination
from .serializers import TodoCreateSerializer, TodoUpdateSerializer


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
        self.queryset = Todo.objects.filter(user_id=self.request.user.id).order_by(
            "-date_created"
        )
        return self.queryset

    def get_serializer_class(self):
        if self.action == "create":
            return TodoCreateSerializer
        return TodoUpdateSerializer
