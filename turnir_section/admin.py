# tournaments/admin.py
from django.contrib import admin
from .models import TeamOne, TeamTwo, Match

@admin.register(TeamOne)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'time', 'tag', 'games_played')

@admin.register(TeamTwo)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'time', 'tag', 'games_played')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team1', 'team2', 'date', 'status', 'score_team1', 'score_team2')
    list_filter = ('status', 'date')
