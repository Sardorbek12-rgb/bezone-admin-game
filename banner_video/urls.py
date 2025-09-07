from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BannerVideoViewSet

router = DefaultRouter()
router.register(r'banner-videos', BannerVideoViewSet, basename='bannervideo')

urlpatterns = [
    path('', include(router.urls)),
]
