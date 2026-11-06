from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_datetime
from .models import Todo
from users.serializers import UserSerializerWithoutId
from users.serializers import UserSerializerWithId


# Add your serializer(s) here
class AllTodoListWithUserDetails(serializers.ModelSerializer):
    creator = UserSerializerWithoutId(source="user")
    status = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ["id", "name", "status", "created_at", "creator"]

    def get_status(self, obj):
        if obj.done:
            return "Done"
        return "To Do"

    def get_created_at(self, obj):

        dt_obj = obj.date_created
        # (%I=12-hour clock, %p=AM/PM, %b=Short month name)
        return dt_obj.strftime("%I:%M %p, %d %b, %Y")


class UserTodoStats(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = list(UserSerializerWithId.Meta.fields) + [
            "completed_count",
            "pending_count",
        ]


class UserPendingTodos(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = list(UserSerializerWithId.Meta.fields) + ["pending_count"]


class UserWithoutIdTodoStats(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = list(UserSerializerWithoutId.Meta.fields) + [
            "pending_count",
            "completed_count",
        ]
