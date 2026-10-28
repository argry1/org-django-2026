from django.conf import settings
from django.db import models


class RewardTransaction(models.Model):

    volunteer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reward_transactions",
    )

    amount = models.IntegerField()

    reason = models.CharField(max_length=255)

    request = models.ForeignKey(
        "requests.HelpRequest",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reward_transactions",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.volunteer} — {self.amount} баллов"