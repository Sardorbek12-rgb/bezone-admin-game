# products/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Category

class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'description', 'cat_image')

translator.register(Category, CategoryTranslationOptions)
