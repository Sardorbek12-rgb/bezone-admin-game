# comments/models.py
from django.db import models

def upload_avatar_path(instance, filename):
    return f"avatars/{instance.name}_{filename}"

class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name=("имя"))
    avatar = models.ImageField(upload_to=upload_avatar_path, blank=True, null=True, verbose_name=("аватар"))
    text = models.TextField(verbose_name=("текст"))
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name=("рейтинг"))
    is_approved = models.BooleanField(default=False, verbose_name=("создано_at"))  # для модерации
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("создано_at"))

    def __str__(self):
        return f"{self.name} ({self.rating})"
