from django.db import models

class Translation(models.Model):
    key = models.CharField(max_length=200, unique=True)
    ru = models.TextField(blank=True)
    uz = models.TextField(blank=True)

    def __str__(self):
        return self.key

class Order(models.Model):
    order = models.CharField(max_length=200, unique=True)
    ru = models.TextField(blank=True)
    uz = models.TextField(blank=True)

    def __str__(self):
        return self.order