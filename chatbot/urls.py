from rest_framework.routers import DefaultRouter
from django.urls import include, path

from chatbot.views import ChatbotView

router = DefaultRouter()
router.register("ask", ChatbotView, basename='ask')


urlpatterns = [
    path('', include(router.urls)),
]