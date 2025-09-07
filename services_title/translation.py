# products/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Card

class CategoryTranslationOptions(TranslationOptions):
    fields = ('icon', 'img', 'title', 'desc')

translator.register(Card, CategoryTranslationOptions)
