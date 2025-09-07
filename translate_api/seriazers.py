from rest_framework import serializers
from .models import Translation

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ('key', 'ru', 'uz')
        ref_name = 'uhsdiuguid'
