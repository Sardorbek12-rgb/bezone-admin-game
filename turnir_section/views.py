# tournaments/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
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

    # 🔹 Все матчи
    @action(detail=False, url_path="all")
    def all_matches(self, request):
        matches = Match.objects.all().order_by("-date")  # последние сверху
        serializer = self.get_serializer(matches, many=True)
        return Response(serializer.data)

    # 🔹 Предстоящие матчи
    @action(detail=False, url_path="upcoming")
    def upcoming(self, request):
        matches = Match.objects.filter(status="upcoming").order_by("date")
        serializer = self.get_serializer(matches, many=True)
        return Response(serializer.data)

    # 🔹 LIVE матчи
    @action(detail=False, url_path="live")
    def live(self, request):
        matches = Match.objects.filter(status="live").order_by("date")
        serializer = self.get_serializer(matches, many=True)
        return Response(serializer.data)

    # 🔹 Завершённые матчи
    @action(detail=False, url_path="finished")
    def finished(self, request):
        matches = Match.objects.filter(status="finished").order_by("-date")
        serializer = self.get_serializer(matches, many=True)
        return Response(serializer.data)
