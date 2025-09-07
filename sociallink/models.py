from django.db import models

class SocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('youtube', 'YouTube'),
        ('telegram', 'Telegram'),
        ('discord', 'Discord'),
        ('twitch', 'Twitch'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='other')
    url = models.URLField()
    icon = models.ImageField(upload_to='social_icons/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.platform}"
