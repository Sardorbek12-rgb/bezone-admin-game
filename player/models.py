from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=150)
    nickname = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    game_name = models.CharField(max_length=100)
    player_position = models.CharField(max_length=100)
    stars = models.PositiveIntegerField(default=0)  # рейтинг (1–5)
    image = models.ImageField(upload_to='players/', blank=True, null=True)

    def __str__(self):
        return f"{self.nickname} ({self.game_name})"

    @property
    def total_matches(self):
        return self.wins + self.draws + self.losses
