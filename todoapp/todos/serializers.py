from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo
from users.serializers import UserSerializerWithoutIdSerializer
from users.serializers import UserSerializerWithIdSerializer
from .constants import TODO_STATUS_PENDING, TODO_STATUS_DONE, DATE_FORMAT

User = get_user_model()


# Add your serializer(s) here
class AllTodoListWithUserDetailsSerializer(serializers.ModelSerializer):
    creator = UserSerializerWithoutIdSerializer(source="user")
    status = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ["id", "name", "status", "created_at", "creator"]

    def get_status(self, obj):
        return TODO_STATUS_DONE if obj.done else TODO_STATUS_PENDING

    def get_created_at(self, obj):
        created_date = obj.date_created
        return created_date.strftime(DATE_FORMAT)


class UserTodoStatsSerializer(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = list(UserSerializerWithIdSerializer.Meta.fields) + [
            "completed_count",
            "pending_count",
        ]


class UserPendingTodosSerializer(UserTodoStatsSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = [
            fields
            for fields in UserTodoStatsSerializer.Meta.fields
            if fields != "completed_count"
        ]


class UserWithoutIdTodoStatsSerializer(UserTodoStatsSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = [
            fields for fields in UserTodoStatsSerializer.Meta.fields if fields != "id"
        ]


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["name", "done", "date_created"]
        read_only_fields = ["done", "date_created"]


class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "name", "done"]
