# tournament/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamOneViewSet, TeamTwoViewSet, MatchViewSet

router = DefaultRouter()
router.register(r'teamsone', TeamOneViewSet)
router.register(r'teamstwo', TeamTwoViewSet)
router.register(r'matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
