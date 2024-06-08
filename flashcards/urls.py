from rest_framework.routers import DefaultRouter
from django.urls import include, path

from flashcards.views import FlashcardsView, CategoryView, DomainsView, CategoryCardViewSet, DomainCardViewSet

router = DefaultRouter()
router.register("flashcards", FlashcardsView, basename='flashcards')
router.register('category', CategoryView, basename='category')
router.register('domains', DomainsView, basename='domains')
router.register('category_card', CategoryCardViewSet, basename='category_card')
router.register('domain_card', DomainCardViewSet, basename='domain_card')

urlpatterns = [
    path('', include(router.urls)),
]