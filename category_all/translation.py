from modeltranslation.translator import translator, TranslationOptions
from .models import ProductCategory

class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'img')  # поля, которые будем переводить

translator.register(ProductCategory, ProductTranslationOptions)
