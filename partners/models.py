from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='company_images/', null=True, blank=True)

    def __str__(self):
        return self.name
