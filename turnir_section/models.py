# tournaments/models.py
from django.db import models
from django.utils import timezone

MATCH_STATUS = (
    ('upcoming', 'Upcoming'),
    ('live', 'Live'),
    ('finished', 'Finished'),
)

class TeamOne(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='teams/')
    games_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class TeamTwo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    tag = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='teams/')
    games_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Match(models.Model):
    team1 = models.ForeignKey(TeamOne, related_name='home_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey(TeamTwo, related_name='away_matches', on_delete=models.CASCADE)
    date = models.DateTimeField()
    code = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=20, choices=MATCH_STATUS, default='upcoming')
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team1} vs {self.team2} - {self.date.strftime('%Y-%m-%d %H:%M')}"
