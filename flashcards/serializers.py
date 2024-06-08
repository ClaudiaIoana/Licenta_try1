
from rest_framework import serializers

from flashcards.models import Domain, Category, Flashcards, CategoryCard, DomainCards


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['id', 'name', 'creator', 'details']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'creator',  'details']


class FlashcardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flashcards
        fields = ['id', 'front', 'back', 'creator', 'category_cards', 'domain_cards', 'archived']


class CategoryCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryCard
        fields = ['id', 'category', 'card']


class GETCategoryCardSerializer(serializers.ModelSerializer):
    front = serializers.CharField(source='card.front')
    back = serializers.CharField(source='card.back')
    id = serializers.IntegerField(source='card.id')

    class Meta:
        model = DomainCards
        fields = ['id', 'front', 'back']


class DomainCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DomainCards
        fields = ['id', 'domain', 'card']


class GETDomainCardSerializer(serializers.ModelSerializer):
    front = serializers.CharField(source='card.front')
    back = serializers.CharField(source='card.back')
    id = serializers.IntegerField(source='card.id')


    class Meta:
        model = DomainCards
        fields = ['id', 'front', 'back']
