from django.db import models


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Team(models.Model):
    colour = models.CharField(max_length=10)
    match_date = models.DateField()
    players = models.ManyToManyField(Member)


class Match(models.Model):
    match_date = models.DateTimeField()
    teams = models.ManyToManyField(Team)
    blue_goals = models.IntegerField(default=0)
    white_goals = models.IntegerField(default=0)
