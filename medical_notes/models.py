from django.db import models

from regular_user.models import RegularUser


class MedicalNotes(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(max_length=100)
    content = models.TextField()
    observations = models.TextField()
    importance = models.IntegerField()
    creator = models.ForeignKey(RegularUser, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        app_label = 'medical_notes'

    def __str__(self):
        return f"{self.title} - {self.topic}"
