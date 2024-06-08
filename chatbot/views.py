import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from chatbot.models import Chat
from chatbot.serializers import ChatSerializer


class ChatbotView(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def create(self, request, *args, **kwargs):
        tokens = Token.objects.all()
        request_data = request.data
        url = "https://qr9c1q8sqv6si0mu.us-east-1.aws.endpoints.huggingface.cloud"
        text = "<om>: " + request_data["question"] + "<asistent>: "
        data = {"inputs": text}
        response = requests.post(url, json=data)
        decoded_response = response.content.decode('utf-8')
        decoded_response = decoded_response[1:]
        decoded_response = decoded_response[:-1]

        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION']
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
        for to in tokens:
            if to.key == token:
                the_user = to.user

        Chat.objects.create(question=request_data['question'], response=decoded_response, creator=the_user)
        return Response({'Response': decoded_response}, status=200)

    def list(self, request, *args, **kwargs):
        tokens = Token.objects.all()
        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION']
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
        for to in tokens:
            if to.key == token:
                the_user = to.user
        if the_user is not None:
            data = Chat.objects.filter(creator=the_user)
            serializer = ChatSerializer(data, many=True)
            return Response(serializer.data)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
