from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False, unique= True)
    email = models.EmailField(max_length=200, null=False, blank=False, unique= True)
    password = models.CharField(max_length=50, null=False, blank=False)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)
    is_in_team = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_logged_in = models.BooleanField(default=False)

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
    players = models.ManyToManyField(Member, blank=True)

    def __str__(self):
        return f"{self.colour} - {self.match_date}"


class Match(models.Model):
    match_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    blue_goals = models.IntegerField(default=0)
    white_goals = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.match_date} - {self.location}"

    class Meta:
        verbose_name_plural = "Matches"



