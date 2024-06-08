from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.utils import json

from medical_notes.models import MedicalNotes
from regular_user.models import RegularUser
from rest_framework.authtoken.models import Token


class QuestionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = RegularUser.objects.create(username='test_user', email='test@example.com')

        self.token = Token.objects.create(user=self.user)
        self.medical_note = MedicalNotes.objects.create(title='Test Note',
                                                        topic='Test Topic',
                                                        content='Test Content',
                                                        observations='Test Observations',
                                                        importance=1,
                                                        creator=self.user)

    def test_create_note(self):
        notes = MedicalNotes.objects.all()
        self.assertEqual(len(notes), 1)

    def test_get_notes(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.key)
        response = self.client.get(reverse('notes-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Note")

    def test_create_note_success(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.key)
        response = self.client.post(reverse('notes-list'), {
            'title': 'New Note',
            'topic': 'New Topic',
            'content': 'New Content',
            'observations': 'New Observations',
            'importance': 2
        })
        self.assertEqual(response.status_code, 201)
        notes = MedicalNotes.objects.all()
        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[1].title, 'New Note')
        self.assertEqual(notes[1].topic, 'New Topic')

    def test_create_note_failure(self):
        response = self.client.post(reverse('notes-list'), {
            'title': 'New Note',
            'content': 'New Content',
            'observations': 'New Observations',
            'importance': 2
        })
        self.assertEqual(response.status_code, 401)
        notes = MedicalNotes.objects.all()
        self.assertEqual(len(notes), 1)

    def test_update_note_success(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.key)
        data = {
            'title': 'Updated Note',
            'topic': 'Updated Topic',
            'content': 'Updated Content',
            'observations': 'Updated Observations',
            'importance': 3
        }
        response = self.client.patch(reverse('notes-detail', args=[self.medical_note.pk]),
                                     data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        updated_note = MedicalNotes.objects.get(pk=self.medical_note.pk)
        self.assertEqual(updated_note.title, 'Updated Note')
        self.assertEqual(updated_note.topic, 'Updated Topic')

    def test_delete_note(self):
        self.client.credentials(HTTP_AUTHORIZATION=self.token.key)
        response = self.client.delete(reverse('notes-detail', args=[self.medical_note.pk]))
        self.assertEqual(response.status_code, 204)
        notes = MedicalNotes.objects.all()
        self.assertEqual(len(notes), 0)
