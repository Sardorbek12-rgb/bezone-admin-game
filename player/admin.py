from django.contrib import admin
from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "nickname", "game_name", "player_position", "wins", "draws", "losses", "stars")
    search_fields = ("name", "nickname", "game_name")
    list_filter = ("game_name", "player_position", "stars")
