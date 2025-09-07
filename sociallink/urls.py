from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SocialLinkViewSet

router = DefaultRouter()
router.register(r'social-links', SocialLinkViewSet, basename='sociallink')

urlpatterns = [
    path('', include(router.urls)),
]
