from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_datetime
from django.utils import timezone
from .models import Todo
from users.serializers import UserSerializerWithoutIdSerializer
from users.serializers import UserSerializerWithIdSerializer


# Add your serializer(s) here
class AllTodoListWithUserDetailsSerializer(serializers.ModelSerializer):
    creator = UserSerializerWithoutIdSerializer(source="user")
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


class UserTodoStatsSerializer(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = list(UserSerializerWithIdSerializer.Meta.fields) + [
            "completed_count",
            "pending_count",
        ]


class UserPendingTodosSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = list(UserSerializerWithIdSerializer.Meta.fields) + ["pending_count"]


class UserWithoutIdTodoStatsSerializer(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = get_user_model()
        fields = list(UserSerializerWithoutIdSerializer.Meta.fields) + [
            "pending_count",
            "completed_count",
        ]


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["name", "user", "done", "date_created"]
        read_only_fields = ["done", "date_created"]
        extra_kwargs = {"user": {"write_only": True}}


class TodoUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["name", "done", "date_created", "date_completed"]
        read_only_fields = ["date_created"]
        #  Hide  from the outgoing GET/POST JSON response
        extra_kwargs = {
            "date_completed": {"write_only": True},
        }


class TodoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["name", "done", "date_created", "user", "date_completed"]
        read_only_fields = ["date_created"]
        #  Hide  from the outgoing GET/POST JSON response
        extra_kwargs = {
            "user": {"write_only": True},
            "date_completed": {"write_only": True},
        }
