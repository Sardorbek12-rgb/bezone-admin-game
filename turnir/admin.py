# tournament/admin.py
from django.contrib import admin
from .models import TeamOne, TeamTwo, Match

@admin.register(TeamOne)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'games_played')

@admin.register(TeamTwo)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'games_played')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'match_date', 'match_time', 'match_code', 'location')
    list_filter = ('match_date',)
