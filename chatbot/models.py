from django.db import models

from regular_user.models import RegularUser


class Chat(models.Model):
    question = models.TextField()
    response = models.TextField()
    creator = models.ForeignKey(RegularUser, on_delete=models.CASCADE)

    class Meta:
        app_label = 'chatbot'

