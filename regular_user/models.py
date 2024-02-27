from django.contrib.auth.models import AbstractUser
from django.db import models


class RegularUser(AbstractUser):
    profile_picture = models.TextField(blank=True)

    class Meta:
        app_label = 'regular_user'

    def __str__(self):
        return f"{self.username}"

