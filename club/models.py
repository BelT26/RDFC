from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ClubMember(AbstractUser):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    is_in_team = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    blues = 'BL'
    whites = 'WH'
    colour_choices = [
        (blues, 'Blues'),
        (whites, 'Whites'),
    ]
    colour = models.CharField(max_length=7, choices=colour_choices)
    match_date = models.DateField()
    players = models.ManyToManyField(ClubMember, blank=True)

    def __str__(self):
        return f"{self.colour} - {self.match_date}"



class Result(models.Model):
    match_date = models.DateField()
    blue_goals = models.IntegerField()
    white_goals = models.IntegerField()


class Match(models.Model):
    match_date = models.DateField()
    time = models.TimeField(default="19:00")
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
    player_id = models.ForeignKey(ClubMember, on_delete=models.CASCADE)
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return f"{self.player_id} - {self.team}"
