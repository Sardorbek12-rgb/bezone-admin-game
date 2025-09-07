from django.urls import path
from .views import TournamentListCreateView, TournamentDetailView

urlpatterns = [
    path("tournaments/", TournamentListCreateView.as_view(), name="tournament-list"),
    path("tournaments/<int:pk>/", TournamentDetailView.as_view(), name="tournament-detail"),
]
