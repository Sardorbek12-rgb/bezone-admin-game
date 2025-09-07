from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView,
    PcBookingCreateView, PcBookingListView,
    NotificationListView,
    PcBookingCreateView,
    PcBookingDetailView,
    PcBookingUpdateView,
    PcBookingDeleteView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("bookings/create/", PcBookingCreateView.as_view(), name="booking-create"),
    path("bookings/", PcBookingListView.as_view(), name="booking-list"),
    path("notifications/", NotificationListView.as_view(), name="notifications"),
    path('bookings/<int:pc_number>/', PcBookingDetailView.as_view(), name='pcbooking-detail'),
    path('bookings/<int:pk>/update/', PcBookingUpdateView.as_view(), name='pcbooking-update'),
    path('bookings/<int:pk>/delete/', PcBookingDeleteView.as_view(), name='pcbooking-delete'),
]
