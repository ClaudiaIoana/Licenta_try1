from rest_framework.routers import DefaultRouter
from django.urls import include, path

from medical_notes.views import MedicalNotesListView

router = DefaultRouter()
router.register('', MedicalNotesListView, basename='notes')

urlpatterns = [
    path('', include(router.urls)),
]