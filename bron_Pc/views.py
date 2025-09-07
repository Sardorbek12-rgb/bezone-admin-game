from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer, LoginSerializer, PcBookingSerializer, NotificationSerializer
from .models import PcBooking, Notification
from rest_framework import generics, permissions

User = get_user_model()  # ✅ вместо auth.User

# --- Регистрация ---
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# --- Логин ---
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return Response({'message': 'Успешный вход'}, status=status.HTTP_200_OK)
        return Response({'error': 'Неверные данные'}, status=status.HTTP_400_BAD_REQUEST)

# --- Логаут ---
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Вы вышли из системы'}, status=status.HTTP_200_OK)

# --- Создание брони ---
class PcBookingCreateView(generics.CreateAPIView):
    serializer_class = PcBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# --- Список броней для пользователя ---
class PcBookingListView(generics.ListAPIView):
    queryset = PcBooking.objects.all()
    serializer_class = PcBookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PcBooking.objects.filter(user=self.request.user)

# --- Уведомления ---
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')


# bron_Pc/views.py
from rest_framework import generics, permissions
from .models import Booking
from .serializers import BookingSerializer

# Создание брони
class PcBookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Просмотр брони по pc_number
class PcBookingDetailView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    lookup_field = 'pc_number'
    permission_classes = [permissions.AllowAny]

# Изменение брони (PATCH/PUT)
class PcBookingUpdateView(generics.UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

# Удаление брони
class PcBookingDeleteView(generics.DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAdminUser]  # только админ

