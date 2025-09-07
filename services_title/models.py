from django.db import models

class Card(models.Model):
    icon = models.ImageField(upload_to='icons/', blank=True, null=True, verbose_name=("икон"))
    img = models.ImageField(upload_to='images/', verbose_name=("фото"))
    title = models.CharField(max_length=255, verbose_name=("заголовок"))
    desc = models.TextField(verbose_name=("описание"))

    def __str__(self):
        return self.title
# 