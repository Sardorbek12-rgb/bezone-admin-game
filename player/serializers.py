from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    total_matches = serializers.ReadOnlyField()

    class Meta:
        model = Player
        fields = "__all__"
