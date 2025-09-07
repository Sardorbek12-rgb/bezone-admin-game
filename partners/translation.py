# products/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Company

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'address')

translator.register(Company, CategoryTranslationOptions)

