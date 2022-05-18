from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class ClubMember(AbstractUser):
    """
    A model used to create a new club member that inherits from
    the django AbstractUser model
    """
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False,
                                 blank=False)
    username = models.CharField(max_length=50, null=False,
                                blank=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    played = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns the first and last name of the club member
        """
        return f"{self.first_name} {self.last_name}"


class Match(models.Model):
    """
    A model used to create match instances
    """
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
        """
        returns the date and the location of the match
        """
        return f"{self.match_date} - {self.location}"

    class Meta:
        """
        Sets the correct plural spelling of the model name
        """
        verbose_name_plural = "Matches"


class MatchPlayer(models.Model):
    """
    Created an instance of a player when a member registers for a
    match
    """
    player_id = models.ForeignKey(ClubMember, on_delete=models.CASCADE,
                                  related_name='matchmember')
    match_id = models.ForeignKey(Match, on_delete=models.CASCADE,
                                 related_name='matchplayer')
    team = models.CharField(max_length=6, null=True, blank=True)
    reserve = models.BooleanField(default=False)
    registration_time = models.DateTimeField(auto_now_add=True)
    win = models.BooleanField(default=False)
    loss = models.BooleanField(default=False)
    draw = models.BooleanField(default=False)
    played = models.BooleanField(default=False)

    def __str__(self):
        """
        returns the name of the player and the team allocated
        """
        return f"{self.player_id} - {self.team}"
