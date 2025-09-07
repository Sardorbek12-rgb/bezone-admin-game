from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import BannerVideo
from .serializers import BannerVideoSerializer

class BannerVideoViewSet(viewsets.ModelViewSet):
    queryset = BannerVideo.objects.all().order_by('-uploaded_at')
    serializer_class = BannerVideoSerializer
    parser_classes = (MultiPartParser, FormParser)
