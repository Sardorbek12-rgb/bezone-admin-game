# tournament/views.py
from rest_framework import viewsets
from .models import TeamOne, TeamTwo, Match
from .serializers import TeamOneSerializer, TeamTwoSerializer, MatchSerializer

class TeamOneViewSet(viewsets.ModelViewSet):
    queryset = TeamOne.objects.all()
    serializer_class = TeamOneSerializer

class TeamTwoViewSet(viewsets.ModelViewSet):
    queryset = TeamTwo.objects.all()
    serializer_class = TeamTwoSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
