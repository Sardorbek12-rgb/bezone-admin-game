from django.contrib import admin
from .models import BannerVideo

@admin.register(BannerVideo)
class BannerVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'uploaded_at')
    readonly_fields = ('uploaded_at',)