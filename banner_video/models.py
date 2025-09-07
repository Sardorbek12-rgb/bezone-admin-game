from django.db import models

class BannerVideo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    video = models.FileField(upload_to='banner_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"BannerVideo {self.pk}"
