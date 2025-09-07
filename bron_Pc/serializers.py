from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PcBooking, Notification

User = get_user_model()

# --- Регистрация ---
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        ref_name = 'profjfjfndsgnjkf'

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user


# --- Логин ---
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        ref_name = 'gewiisjsfinjdsjdsg'

class PcBookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = PcBooking
        fields = "__all__"
        ref_name = 'eragofovjnjdfngj'

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["user"] = request.user  # 👈 автоматически берем юзера
        return super().create(validated_data)

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Notification
        fields = "__all__"
        ref_name = 'gdoigjigidjfnijfg'


# bron_Pc/serializers.py
from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Booking
        fields = ['id', 'user', 'pc_number', 'tariff', 'booking_date', 'booking_time']
