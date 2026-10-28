from django.conf import settings
from django.db import models


class Partner(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="partners",
    )

    organization_name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    address = models.CharField(max_length=255)

    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.organization_name


class PartnerOffer(models.Model):
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="offers",
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    points_cost = models.PositiveIntegerField()

    valid_until = models.DateField(
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.partner} — {self.title}"


class PartnerApplication(models.Model):

    class Status(models.TextChoices):
        NEW = "new", "Новая"
        APPROVED = "approved", "Одобрена"
        REJECTED = "rejected", "Отклонена"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="partner_applications",
    )

    email = models.EmailField(blank=True)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Обращение от {self.user}"