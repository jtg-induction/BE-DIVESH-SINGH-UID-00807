from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Todo
from users.serializers import UserSerializerWithoutIdSerializer
from users.serializers import UserSerializerWithIdSerializer

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
        model = User
        fields = list(UserSerializerWithIdSerializer.Meta.fields) + [
            "completed_count",
            "pending_count",
        ]


class UserPendingTodosSerializer(serializers.ModelSerializer):
    pending_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = list(UserSerializerWithIdSerializer.Meta.fields) + ["pending_count"]


class UserWithoutIdTodoStatsSerializer(serializers.ModelSerializer):
    completed_count = serializers.IntegerField()
    pending_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = list(UserSerializerWithoutIdSerializer.Meta.fields) + [
            "pending_count",
            "completed_count",
        ]
