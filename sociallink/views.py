from rest_framework import viewsets
from .models import SocialLink
from .serialzers import SocialLinkSerializer

class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
