from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Project, ProjectMember
from todos.serializers import UserWithoutIdTodoStats
from users.serializers import UserSerializerWithoutId


class ProjectsDetails(serializers.ModelSerializer):
    existing_member_count = serializers.IntegerField()
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Project
        fields = ["id", "name", "status", "existing_member_count", "max_members"]


class ProjectReport(serializers.ModelSerializer):
    report = UserWithoutIdTodoStats(source="members", many=True)
    project_title = serializers.CharField(source="name")

    class Meta:
        model = Project
        fields = ["project_title", "report"]


class ProjectStatus(serializers.ModelSerializer):
    to_do_projects = serializers.ListField()
    in_progress_projects = serializers.ListField()
    completed_projects = serializers.ListField()

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
            "to_do_projects",
            "in_progress_projects",
            "completed_projects",
        ]
