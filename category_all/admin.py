from django.contrib import admin
from . import translation

from modeltranslation.admin import TranslationAdmin
from .models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'img')
    prepopulated_fields = {"slug": ("name",)}
