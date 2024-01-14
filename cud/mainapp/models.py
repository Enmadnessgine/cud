from django.db import models

class PlayerCoordinates(models.Model):
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)