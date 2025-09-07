from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('-stars')
    serializer_class = PlayerSerializer
