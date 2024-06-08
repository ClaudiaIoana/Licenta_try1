from medical_notes.models import MedicalNotes
from rest_framework import serializers


class MedicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNotes
        fields = ['id', 'title', 'topic', 'content', 'observations', 'importance', 'creator']
