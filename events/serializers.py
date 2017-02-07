from rest_framework import serializers
from events.models import Event
from users.models import User

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='get_event_owner') 
    class Meta:
        model = Event
        fields = ( 'id', 'name', 'owner', 'created_at', 'updated_at')
