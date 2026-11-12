from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.utils import timezone
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
        elif self.action in ["update", "partial_update"]:
            return TodoUpdateSerializer

        # Fallback serializer for list/retrieve actions
        return TodoCreateSerializer

    def perform_update(self, serializer):
        current_instance = self.get_object()
        if current_instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to edit this todo.")
        new_done_status = serializer.validated_data.get("done", current_instance.done)
        if new_done_status and not current_instance.done:
            date_completed = timezone.now()
        elif not new_done_status:
            date_completed = None
        else:
            date_completed = current_instance.date_completed
        serializer.save(date_completed=date_completed)

    def perform_destroy(self, instance):
        current_instance = self.get_object()
        if current_instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this todo.")
        return super().perform_destroy(instance)
