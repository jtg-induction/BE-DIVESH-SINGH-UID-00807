# This gives us a specialized test class for testing APIs
from rest_framework.test import APITestCase

# This helps us generate the URLs automatically instead of hardcoding them
from django.urls import reverse

# This provides standard HTTP status numbers (like 200 for OK, 201 for Created)
from rest_framework import status
from django.contrib.auth import get_user_model
from todos.models import Todo


class TodoAPIViewSet(APITestCase):
    def setUp(self):
        self.list_url = reverse("todos:todos-list")
        User = get_user_model()
        self.test_user = User.objects.create_user(
            email="test@example.com", password="password123", id=456
        )
        self.test_todo = Todo.objects.create(
            name="Buy milk", done=False, user=self.test_user
        )
        self.detail_url = reverse(
            "todos:todos-detail", kwargs={"pk": self.test_todo.pk}
        )

    def test_can_create_a_new_todo(self):
        self.client.force_authenticate(user=self.test_user)
        data = {"name": "Learn Django Testing"}
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Todo.objects.filter(name="Learn Django Testing").exists())

    def test_can_not_create_a_new_todo(self):
        self.client.force_authenticate(user=self.test_user)
        data = {}
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_data(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_a_todo(self):
        self.client.force_authenticate(user=self.test_user)
        data = {"done": True}
        response = self.client.patch(self.detail_url, data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.test_todo.refresh_from_db()
        self.assertTrue(self.test_todo.done)

    def test_data_with_user_id(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, response.data["count"])

    def test_can_delete_a_todo(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_an_unauthorized_access(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
