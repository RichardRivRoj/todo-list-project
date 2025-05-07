from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

class TaskAPITestCase(APITestCase):
    def setUp(self):
        # Crear usuario de prueba
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )
        # Autenticar al usuario
        self.client.force_authenticate(user=self.user)
        # Crear tarea de prueba
        self.task = Task.objects.create(
            title="Tarea de prueba",
            user=self.user
        )

    def test_list_tasks(self):
        url = reverse('task-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Debe retornar la tarea creada en setUp

    def test_create_task(self):
        url = reverse('task-list-create')
        data = {
            "title": "Nueva tarea",
            "description": "Descripción de prueba"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)  # La tarea de setUp + esta nueva

    def test_delete_task(self):
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)