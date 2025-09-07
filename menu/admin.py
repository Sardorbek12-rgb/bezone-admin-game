from django.contrib import admin
from .models import Category, Product, CartItem, WishlistItem, Order, OrderItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(WishlistItem)
admin.site.register(Order)
admin.site.register(OrderItem)
