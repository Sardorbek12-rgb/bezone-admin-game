from django.urls import path
from .views import TranslationListAPIView

urlpatterns = [
    path('translations/', TranslationListAPIView.as_view(), name='translations-list'),
]
