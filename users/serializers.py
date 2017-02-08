from rest_framework import serializers
from users.models import User
from events.models import Event

class UserSerializer(serializers.HyperlinkedModelSerializer):
    events_owned = serializers.HyperlinkedRelatedField(view_name="event-detail", read_only=True, many=True)
    participating_in = serializers.HyperlinkedRelatedField(view_name="event-detail", read_only=True, many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'events_owned', 'participating_in',)
