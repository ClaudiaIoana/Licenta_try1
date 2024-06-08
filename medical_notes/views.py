from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import authenticate

from medical_notes.models import MedicalNotes
from medical_notes.serializers import MedicalNoteSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


# Create your views here.
class MedicalNotesListView(viewsets.ModelViewSet):
    queryset = MedicalNotes.objects.all()
    serializer_class = MedicalNoteSerializer

    def list(self, request, *args, **kwargs):
        the_user = None
        tokens = Token.objects.all()
        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION']
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
        for to in tokens:
            if to.key == token:
                the_user = to.user
        if the_user is not None:
            medical_notes = MedicalNotes.objects.filter(creator=the_user.id)
            serializer = MedicalNoteSerializer(medical_notes, many=True)
            return Response(serializer.data)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)

    def create(self, request, *args, **kwargs):
        the_user = None
        tokens = Token.objects.all()
        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION']
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
        for to in tokens:
            if to.key == token:
                the_user = to.user
        if the_user is None:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)

        return super().create(request)

    def update(self, request, *args, **kwargs):
        the_user = None
        tokens = Token.objects.all()
        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION']
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
        for to in tokens:
            if to.key == token:
                the_user = to.user
        if the_user is None:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)

        return super().update(request)

    def delete(self, request, *args, **kwargs):
        the_user = None
        tokens = Token.objects.all()
        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION']
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
        for to in tokens:
            if to.key == token:
                the_user = to.user
        if the_user is None:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)

        return super().destroy(request)





