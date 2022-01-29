from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ClubMember(AbstractUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Match(models.Model):
    match_date = models.DateField()
    time = models.TimeField(default="20:00")
    location = models.CharField(max_length=200)
    blue_goals = models.IntegerField(default=0)
    white_goals = models.IntegerField(default=0)
    results_added = models.BooleanField(default=False)
    registrations_open = models.BooleanField(default=False)
    next_fixture = models.BooleanField(default=False)
    teams_allocated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.match_date} - {self.location}"

    class Meta:
        verbose_name_plural = "Matches"


class MatchPlayer(models.Model):
    player_id = models.ForeignKey(ClubMember, on_delete=models.CASCADE, related_name='matchmember')
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='matchplayer')
    team = models.CharField(max_length=6, null=True, blank=True)
    reserve = models.BooleanField(default=False)
    registration_time = models.DateTimeField(auto_now_add=True)
    win = models.BooleanField(default=False)
    loss = models.BooleanField(default=False)
    draw = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.player_id} - {self.team}"
