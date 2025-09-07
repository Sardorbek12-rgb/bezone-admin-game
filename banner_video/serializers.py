from rest_framework import serializers
from .models import BannerVideo

class BannerVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerVideo
        fields = ['id', 'title', 'video', 'uploaded_at']
