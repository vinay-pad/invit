from rest_framework import serializers
from users.models import User
from events.models import Event

class UserSerializer(serializers.ModelSerializer):
    events_owned = serializers.PrimaryKeyRelatedField(queryset=Event.objects.all(),many=True)
    user_id = serializers.ReadOnlyField(source='get_user_id')
    class Meta:
        model = User
        fields = ('username', 'events_owned', 'user_id',)
