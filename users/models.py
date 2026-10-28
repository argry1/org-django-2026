
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        PENSIONER = "pensioner", "Пенсионер"
        VOLUNTEER = "volunteer", "Волонтёр"
        PARTNER = "partner", "Партнёр"
        ADMIN = "admin", "Администратор"

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PENSIONER,
    )