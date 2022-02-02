from pyexpat import model
from django.db import models


class Game(models.Model):
    room_code = models.CharField(max_length=100)
    game_creator = models.CharField(max_length=100)
    game_oppononet = models.CharField(max_length=100, blank=True, null=True)
    is_over = models.BooleanField(default=False)
    prefrence = models.CharField(max_length=2, blank=True, null=True)


class Room(models.Model):
    room = models.CharField(max_length=100, unique=True)
    connected_users = models.IntegerField(blank=True, null=True, default="0")
