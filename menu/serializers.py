from rest_framework import serializers
from .models import Product, Category, CartItem, WishlistItem, Order, OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ["id", "title", "price", "popularity", "rating", "category", 'image']

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_id', 'quantity']

class WishlistItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # для отображения продукта
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = WishlistItem
        fields = ['id', 'product', 'product_id']


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)
    title = serializers.CharField(source='product.title', read_only=True)
    price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'title', 'price', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'cabinet', 'room', 'seat', 'order_type', 'total', 'created_at', 'items']
        read_only_fields = ['user', 'total', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user
        total = sum([item['product'].price * item['quantity'] for item in items_data])
        order = Order.objects.create(user=user, total=total, **validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order