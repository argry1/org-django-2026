from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    name = models.CharField(max_length=50)
    is_done = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

