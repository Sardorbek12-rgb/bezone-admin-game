from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Address

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1
    fields = ('street', 'city', 'country')

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительно", {"fields": ("phone_number", "image")}),
    )
    list_display = ("username", "password", "phone_number")
    inlines = [AddressInline]