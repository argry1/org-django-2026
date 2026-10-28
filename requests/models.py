from django.conf import settings
from django.db import models


class HelpRequest(models.Model):

    class Category(models.TextChoices):
        PRODUCTS = "products", "Покупка продуктов"
        MEDICINES = "medicines", "Покупка лекарств"
        HOME = "home", "Помощь по дому"
        ACCOMPANIMENT = "accompaniment", "Сопровождение"
        TECH = "tech", "Помощь с техникой"
        COMMUNICATION = "communication", "Общение"
        OTHER = "other", "Другое"

    class Status(models.TextChoices):
        OPEN = "open", "Открыта"
        IN_PROGRESS = "in_progress", "В работе"
        COMPLETED = "completed", "Выполнена"
        CANCELLED = "cancelled", "Отменена"

    pensioner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="help_requests",
    )

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=Category.choices,
    )

    address = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    completed_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

class Application(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Ожидает решения"
        ACCEPTED = "accepted", "Принята"
        REJECTED = "rejected", "Отклонена"
        WAITING_CONFIRMATION = "waiting_confirmation", "Ждёт подтверждения"
        COMPLETED = "completed", "Выполнена"

    request = models.ForeignKey(
        HelpRequest,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    volunteer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.volunteer} — {self.request}"