from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Project, ProjectMember

User = get_user_model()


class ProjectMemberApiTests(APITestCase):
    def setUp(self):
        self.url = "/api/projects/"
        self.admin = User.objects.create_superuser(
            email="admin@test.com", password="password123"
        )
        self.user1 = User.objects.create_user(
            email="u1@test.com", password="password123"
        )
        self.user2 = User.objects.create_user(
            email="u2@test.com", password="password123"
        )
        self.user3 = User.objects.create_user(
            email="u3@test.com", password="password123"
        )
        self.user4 = User.objects.create_user(
            email="u4@test.com", password="password123"
        )
        self.project_main = Project.objects.create(name="Main Project", max_members=2)
        self.project_other_1 = Project.objects.create(name="Other 1", max_members=5)
        self.project_other_2 = Project.objects.create(name="Other 2", max_members=5)
        self.client.force_authenticate(user=self.admin)

    def test_unauthenticated_user_denied(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(
            f"{self.url}?id={self.project_main.id}",
            {"user_ids": [self.user1.id]},
        )
        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED],
        )

    def test_non_admin_user_denied(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(
            f"{self.url}?id={self.project_main.id}",
            {"user_ids": [self.user1.id]},
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_missing_or_invalid_project_id_query_param(self):
        # Missing ?id=
        res_missing = self.client.post(
            self.url,
            {"user_ids": [self.user1.id]},
        )
        self.assertEqual(res_missing.status_code, status.HTTP_400_BAD_REQUEST)

        # Non-digit ?id=abc
        res_invalid = self.client.post(
            f"{self.url}?id=abc",
            {"user_ids": [self.user1.id]},
        )
        self.assertEqual(res_invalid.status_code, status.HTTP_400_BAD_REQUEST)

    def test_project_not_found(self):
        response = self.client.post(
            f"{self.url}?id=99999",
            {"user_ids": [self.user1.id]},
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["error"], "Project Not Found")

    def test_add_members_success(self):
        response = self.client.post(
            f"{self.url}?id={self.project_main.id}",
            {"user_ids": [self.user1.id, self.user2.id]},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data["logs"],
            {
                self.user1.id: "Member added Successfully",
                self.user2.id: "Member added Successfully",
            },
        )
        self.assertEqual(
            ProjectMember.objects.filter(project=self.project_main).count(), 2
        )

    def test_add_members_all_constraints_and_edge_cases(self):
        ProjectMember.objects.create(project=self.project_main, member=self.user1)
        ProjectMember.objects.create(project=self.project_other_1, member=self.user2)
        ProjectMember.objects.create(project=self.project_other_2, member=self.user2)

        # Send mixed batch:
        # - user1: already a member
        # - user2: already in 2 projects
        # - user3: valid -> fills the 2nd and final slot of project_main
        # - user4: valid -> rejected because project_main is now full (max_members=2)
        # - 9999: non-existent user
        payload_ids = [
            self.user1.id,
            self.user2.id,
            self.user3.id,
            self.user4.id,
            9999,
        ]
        response = self.client.post(
            f"{self.url}?id={self.project_main.id}",
            {"user_ids": payload_ids},
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        logs = response.data["logs"]
        self.assertEqual(logs[self.user1.id], "User is already a Member")
        self.assertEqual(
            logs[self.user2.id], "Cannot add as User is a member in two projects"
        )
        self.assertEqual(logs[self.user3.id], "Member added Successfully")
        self.assertEqual(logs[self.user4.id], "Project is Already Full")
        self.assertEqual(logs[9999], "Not Found User")

    def test_add_members_returns_200_when_none_added(self):
        ProjectMember.objects.create(project=self.project_main, member=self.user1)
        response = self.client.post(
            f"{self.url}?id={self.project_main.id}",
            {"user_ids": [self.user1.id, 9999]},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_members_mixed_cases(self):
        ProjectMember.objects.create(project=self.project_main, member=self.user1)

        response = self.client.patch(
            f"{self.url}?id={self.project_main.id}",
            {"user_ids": [self.user1.id, self.user2.id, 9999]},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        logs = response.data["logs"]
        self.assertEqual(logs[self.user1.id], "Member Removed Successfully")
        self.assertEqual(logs[self.user2.id], "User is Not a Member")
        self.assertEqual(logs[9999], "Not Found User")
        self.assertFalse(
            ProjectMember.objects.filter(
                project=self.project_main, member=self.user1
            ).exists()
        )
