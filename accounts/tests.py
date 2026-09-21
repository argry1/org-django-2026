from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

# Create your tests here.
class Todotest(TestCase):

    def test_create_task(self):
        user = User.objects.create_user(
            username="alice",
            password="12345"
        )

        task = Task.objects.create(
            name="Выучить тесты",
            author=user
        )

        self.assertEqual(task.name, "Выучить тесты")
        self.assertEqual(task.author, user)