import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.db import models
from django.utils import timezone
from users.models import User

class Event(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name="events_owned", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(null=True)
    participants = models.ManyToManyField(User, through='membership.Membership', related_name="participating_in")

    def save(self, *args, **kwargs):
        if not self.id:
            logger.debug("Event "+str(self.name)+" created.")
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Event, self).save(*args, **kwargs)

