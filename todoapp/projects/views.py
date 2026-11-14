from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Count
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, ProjectMember
from .serializers import AddProjectMemberSerializer

User = get_user_model()


class ProjectMemberApiViewSet(APIView):
    """
    constraints
     - a user can be a member of max 2 projects only
     - a project can have at max N members defined in database for each project
    functionalities
    - add users to projects

      Request
      { user_ids: [1,2,...n] }
      Response
      {
        logs: {
          <user_id>: <status messages>
        }
      }
      following are the possible status messages
      case1: if user is added successfully then - "Member added Successfully"
      case2: if user is already a member then - "User is already a Member"
      case3: if user is already added to 2 projects - "Cannot add as User is a member in two projects"

      there will be many other cases think of that

    - update to remove users from projects

      Request
      { user_ids: [1,2,...n] }

      Response
      {
        logs: {
          <user_id>: <status messages>
        }
      }

      there will be many other cases think of that and share on forum
    """

    permission_classes = [IsAdminUser]

    def _validate_request(self, request):
        serializer = AddProjectMemberSerializer(data=request.data)
        if not serializer.is_valid():
            return (
                None,
                None,
                Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST),
            )

        project_id = request.query_params.get("id")
        if not project_id or not str(project_id).isdigit():
            return (
                None,
                None,
                Response(
                    {"error": "Valid project id query parameter is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                ),
            )

        return set(serializer.validated_data["user_ids"]), int(project_id), None

    def _get_locked_context(self, project_id, user_ids):
        project = Project.objects.select_for_update().filter(id=project_id).first()
        if project is None:
            return None, None, None

        valid_user_ids = set(
            User
            .objects.select_for_update()
            .filter(id__in=user_ids)
            .values_list("id", flat=True)
        )
        existing_members = set(
            ProjectMember.objects.filter(
                project_id=project_id, member_id__in=valid_user_ids
            ).values_list("member_id", flat=True)
        )
        return project, valid_user_ids, existing_members

    def post(self, request):
        user_ids, project_id, error_response = self._validate_request(request)
        if error_response:
            return error_response

        with transaction.atomic():
            project, valid_user_ids, existing_members = self._get_locked_context(
                project_id, user_ids
            )
            if project is None:
                return Response(
                    {"error": "Project Not Found"}, status=status.HTTP_404_NOT_FOUND
                )

            existing_member_count = ProjectMember.objects.filter(
                project_id=project_id
            ).count()
            user_project_counts = dict(
                ProjectMember.objects.filter(member_id__in=valid_user_ids)
                .values_list("member_id")
                .annotate(project_count=Count("id"))
            )

            data = {}
            new_members = []
            for u in user_ids:
                if u not in valid_user_ids:
                    data[u] = "Not Found User"
                elif u in existing_members:
                    data[u] = "User is already a Member"
                elif user_project_counts.get(u, 0) >= 2:
                    data[u] = "Cannot add as User is a member in two projects"
                elif existing_member_count >= project.max_members:
                    data[u] = "Project is Already Full"
                else:
                    new_members.append(
                        ProjectMember(member_id=u, project_id=project_id)
                    )
                    existing_member_count += 1
                    data[u] = "Member added Successfully"

            if new_members:
                ProjectMember.objects.bulk_create(new_members)

        response_status = status.HTTP_201_CREATED if new_members else status.HTTP_200_OK
        return Response({"logs": data}, status=response_status)

    def patch(self, request):
        user_ids, project_id, error_response = self._validate_request(request)
        if error_response:
            return error_response

        with transaction.atomic():
            project, valid_user_ids, existing_members = self._get_locked_context(
                project_id, user_ids
            )
            if project is None:
                return Response(
                    {"error": "Project Not Found"}, status=status.HTTP_404_NOT_FOUND
                )

            data = {}
            remove_members = []
            for u in user_ids:
                if u not in valid_user_ids:
                    data[u] = "Not Found User"
                elif u not in existing_members:
                    data[u] = "User is Not a Member"
                else:
                    remove_members.append(u)
                    data[u] = "Member Removed Successfully"

            if remove_members:
                ProjectMember.objects.filter(
                    member_id__in=remove_members, project_id=project_id
                ).delete()

        return Response({"logs": data}, status=status.HTTP_200_OK)
