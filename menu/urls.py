from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    ProductViewSet,
    CartItemViewSet,
    WishlistItemViewSet,
    OrderViewSet,
    OrderViewSet,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'cart', CartItemViewSet, basename='cart')
router.register(r'wishlist', WishlistItemViewSet, basename='wishlist')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
]
