from django.db import models
from events.models import Event

class Participators(models.Model):
    user = models.ForeignKey('auth.User', related_name="participating", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name="participants", on_delete=models.CASCADE)
