from django.db import models

class Location(models.Model):
    name = models.CharField("Имя", max_length=255)
    address = models.TextField("Адресс",blank=True, null=True)
    latitude = models.DecimalField("Широта",max_digits=9, decimal_places=6)
    longitude = models.DecimalField("Долгота",max_digits=9, decimal_places=6)
    iframe = models.TextField("Локация iframe", help_text="Вставьте HTML iframe-код карты")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Локация-места'
        verbose_name_plural = 'Локация-места'