from django.db import models
from django.conf import settings

TARIFF_CHOICES = [
    ('standard', 'Стандарт'),
    ('standard_plus', 'Стандарт+'),
    ('vip', 'VIP'),
    ('console', 'Приставка'),
]

class PcBooking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    tariff = models.CharField(max_length=20, choices=TARIFF_CHOICES)
    pc_number = models.PositiveIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - ПК {self.pc_number} - {self.tariff}"

class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications'
    )
    message = models.TextField()
    tariff = models.CharField(max_length=20, choices=TARIFF_CHOICES)
    pc_number = models.PositiveIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Уведомление для {self.user.username} - {self.message[:20]}"


from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='book'
    )
    pc_number = models.PositiveIntegerField()
    tariff = models.CharField(max_length=50)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['pc_number', 'booking_date', 'booking_time']

    def __str__(self):
        return f"ПК {self.pc_number} - {self.user.username}"