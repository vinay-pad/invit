import logging
logger = logging.getLogger(__name__)
from django.db import models
from users.models import User
from events.models import Event
from django.utils import timezone

class Membership(models.Model):

    MEMBERSHIP_STATUS_INVITED=1
    MEMBERSHIP_STATUS_GOING=2
    MEMBERSHIP_STATUS_DECLINED=3

    MEMBERSHIP_STATUS = (
            (MEMBERSHIP_STATUS_INVITED, "Invited"),
            (MEMBERSHIP_STATUS_GOING, "Going"),
            (MEMBERSHIP_STATUS_DECLINED, "Not going"),
            )
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(null=True)
    status = models.SmallIntegerField(choices=MEMBERSHIP_STATUS, default=MEMBERSHIP_STATUS_INVITED)

    def save(self, *args, **kwargs):
        if not self.id:
            logger.debug("Membership "+str(self.event)+" created.")
            self.date_joined = timezone.now()
        return super(Membership, self).save(*args, **kwargs)
