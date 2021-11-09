from django.conf import settings
from django.db import models


class Repetition(models.Model):
    "Generated Model"
    exercise = models.CharField(
        max_length=5,
    )
    weight = models.IntegerField()
    repetitions = models.IntegerField()
