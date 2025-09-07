from django.contrib import admin
from .models import PcBooking, Notification

@admin.register(PcBooking)
class PcBookingAdmin(admin.ModelAdmin):
    list_display = ("user", "pc_number", "tariff", "booking_date", "booking_time", "is_approved", "created_at")
    list_filter = ("tariff", "is_approved", "booking_date")

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "message", "tariff", "pc_number", "booking_date", "booking_time", "is_approved", "created_at")
    list_filter = ("tariff", "is_approved", "booking_date")

# bron_Pc/admin.py
from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'pc_number', 'tariff', 'booking_date', 'booking_time', 'created_at']
    list_filter = ['pc_number', 'tariff', 'booking_date']
    search_fields = ['user__username', 'pc_number']