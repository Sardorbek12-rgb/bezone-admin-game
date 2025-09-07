# tournament/models.py
from django.db import models

class TeamOne(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='team_images/')
    games_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class TeamTwo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='team_images/')
    games_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Match(models.Model):
    team1 = models.ForeignKey(TeamOne, related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(TeamTwo, related_name='team2_matches', on_delete=models.CASCADE)
    match_time = models.CharField(max_length=100)
    match_date = models.CharField(max_length=100)
    match_code = models.CharField(max_length=20)
    location = models.CharField(max_length=50, default='PC')  # или AM

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} ({self.match_date})"
