# tournament/serializers.py
from rest_framework import serializers
from .models import TeamOne, Match, TeamTwo

class TeamOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOne
        fields = '__all__'

class TeamTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamTwo
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamOneSerializer(read_only=True)
    team2 = TeamTwoSerializer(read_only=True)

    class Meta:
        model = Match
        fields = '__all__'
