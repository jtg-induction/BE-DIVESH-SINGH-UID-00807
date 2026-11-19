from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError,NotFound
from .models import Todo
from .pagination import StandardResultsSetPagination
from .serializers import TodoCreateSerializer
from .constants import USER_ID_MUST_BE_POSITIVE,NO_TODOS_FOR_USER


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
    serializer_class=TodoCreateSerializer

    def get_queryset(self):
        self.queryset = Todo.objects.all().order_by("-date_created")
        user_id = self.request.query_params.get("user_id")
        if user_id:
            try:
                user_id = int(user_id)
                if(user_id<=0):
                    raise ValueError
            except ValueError:
                raise ValidationError({"error":USER_ID_MUST_BE_POSITIVE})
            self.queryset = Todo.objects.filter(user_id=user_id).order_by("-date_created")
            if not self.queryset.exists():
                raise NotFound({"error":NO_TODOS_FOR_USER})
        return self.queryset
    