from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Category, Product, CartItem, WishlistItem, Order, OrderItem
from .serializers import CategorySerializer, ProductSerializer, CartItemSerializer, WishlistItemSerializer, OrderSerializer
from rest_framework.decorators import action

# Category и Product без изменений
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()

        # фильтрация по категории
        category = self.request.query_params.get("category")
        if category and category != "all":
            queryset = queryset.filter(category__slug=category)

        # сортировка
        sort = self.request.query_params.get("sort")
        if sort == "price":
            queryset = queryset.order_by("price")
        elif sort == "price-desc":
            queryset = queryset.order_by("-price")
        elif sort == "rating":
            queryset = queryset.order_by("-rating")
        elif sort == "popularity":
            queryset = queryset.order_by("-popularity")
        elif sort == "date":
            queryset = queryset.order_by("-created_at")

        return queryset

# CartItem
class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# WishlistItem
class WishlistItemViewSet(viewsets.ModelViewSet):
    serializer_class = WishlistItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WishlistItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)