# tournaments/serializers.py
from rest_framework import serializers
from .models import TeamOne, TeamTwo, Match

class TeamOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamOne
        fields = '__all__'
        ref_name = 'gggggsgdfg'

class TeamTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamTwo
        fields = '__all__'
        ref_name = 'uijsuffgkdfggkndfbgj'

class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamOneSerializer()
    team2 = TeamTwoSerializer()

    class Meta:
        model = Match
        fields = '__all__'
        ref_name = 'sugsdhubhsbghbuhgbdhug'