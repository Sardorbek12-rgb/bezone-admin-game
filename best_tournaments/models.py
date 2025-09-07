from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="tournaments/")
    description = models.TextField()

    def __str__(self):
        return self.name
