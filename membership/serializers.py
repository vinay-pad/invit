from rest_framework import serializers
from membership.models import Membership
from events.models import Event

class MembershipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        fields = ('person', 'event', 'date_joined', 'status',)
