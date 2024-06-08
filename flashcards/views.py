from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets

from flashcards.models import Flashcards, Domain, Category, CategoryCard, DomainCards
from flashcards.serializers import FlashcardSerializer, DomainSerializer, CategorySerializer, CategoryCardSerializer, \
    DomainCardSerializer, GETDomainCardSerializer, GETCategoryCardSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class FlashcardsView(viewsets.ModelViewSet):
    queryset = Flashcards.objects.all()
    serializer_class = FlashcardSerializer

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
            request_data = self.request.GET
            if 'domain' in request_data:
                medical_notes = DomainCards.objects.filter(domain=int(request_data['domain']))
                medical_notes = medical_notes.filter(card__archived=False)
                serializer = GETDomainCardSerializer(medical_notes, many=True)
                return Response(serializer.data)
            if 'criteria' in request_data:
                medical_notes = CategoryCard.objects.filter(category=int(request_data['criteria']))
                medical_notes = medical_notes.filter(card__archived=False)
                serializer = GETCategoryCardSerializer(medical_notes, many=True)
                return Response(serializer.data)
            if 'archived' in request_data:
                if request_data['archived']:
                    medical_notes = Flashcards.objects.filter(creator=the_user.id)
                    medical_notes = medical_notes.filter(archived=True)
                    serializer = FlashcardSerializer(medical_notes, many=True)
                    return Response(serializer.data)
            medical_notes = Flashcards.objects.filter(creator=the_user.id)
            medical_notes = medical_notes.filter(archived=False)
            serializer = FlashcardSerializer(medical_notes, many=True)
            return Response(serializer.data)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)


class DomainsView(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer

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
            request_data = self.request.GET
            medical_notes = Domain.objects.filter(creator=the_user.id)
            serializer = DomainSerializer(medical_notes, many=True)
            return Response(serializer.data)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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
            request_data = self.request.GET
            medical_notes = Category.objects.filter(creator=the_user.id)
            serializer = CategorySerializer(medical_notes, many=True)
            return Response(serializer.data)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)


class CategoryCardViewSet(viewsets.ModelViewSet):
    queryset = CategoryCard.objects.all()
    serializer_class = CategoryCardSerializer

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
            request_data = self.request.GET
            if 'criteria' in request_data:
                medical_notes = Flashcards.objects.filter(creator=the_user.id).exclude(category_cards__id=int(request_data['criteria']))
                medical_notes = medical_notes.filter(archived=False)
                serializer = FlashcardSerializer(medical_notes, many=True)
                return Response(serializer.data)
            medical_notes = Flashcards.objects.filter(creator=the_user.id)
            medical_notes = medical_notes.filter(archived=False)
            serializer = FlashcardSerializer(medical_notes, many=True)
            return Response(serializer.data)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)

    def destroy(self, request, *args, **kwargs):
        tokens = Token.objects.all()

        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION']
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
        for to in tokens:
            if to.key == token:
                the_user = to.user
        if the_user is not None:
            request_data = self.request.data
            if 'card' not in request_data:
                return Response({'Unauthorized': 'Unauthorized'}, status=401)
            if 'criteria' not in request_data:
                return Response({'Unauthorized': 'Unauthorized'}, status=401)
            to_remove = CategoryCard.objects.filter(category=int(request_data['criteria']))
            to_remove = to_remove.filter(card=int(request_data['card']))
            to_remove.delete()
            return Response({'Status': 'Succesful'}, status=200)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)


class DomainCardViewSet(viewsets.ModelViewSet):
    queryset = DomainCards.objects.all()
    serializer_class = DomainCardSerializer

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
            request_data = self.request.GET
            if 'domain' in request_data:
                medical_notes = Flashcards.objects.filter(creator=the_user.id).exclude(domain_cards__id=int(request_data['domain']))
                medical_notes = medical_notes.filter(archived=False)
                serializer = FlashcardSerializer(medical_notes, many=True)
                return Response(serializer.data)
            medical_notes = Flashcards.objects.filter(creator=the_user.id)
            medical_notes = medical_notes.filter(archived=False)
            serializer = FlashcardSerializer(medical_notes, many=True)
            return Response(serializer.data)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)

    def destroy(self, request, *args, **kwargs):
        tokens = Token.objects.all()

        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META['HTTP_AUTHORIZATION']
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)
        for to in tokens:
            if to.key == token:
                the_user = to.user
        if the_user is not None:
            request_data = self.request.data
            if 'card' not in request_data:
                return Response({'Unauthorized': 'Unauthorized'}, status=401)
            if 'domain' not in request_data:
                return Response({'Unauthorized': 'Unauthorized'}, status=401)
            to_remove = DomainCards.objects.filter(domain=int(request_data['domain']))
            to_remove = to_remove.filter(card=int(request_data['card']))
            to_remove.delete()
            return Response({'Status': 'Succesful'}, status=200)
        else:
            return Response({'Unauthorized': 'Unauthorized'}, status=401)



