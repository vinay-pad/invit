from rest_framework import serializers
from events.models import Event
from users.models import User
from users.serializers import UserSerializer
from users.views import UserList
from membership.models import Membership

class EventSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    #owner = serializers.StringRelatedField(required=False)
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    participants = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True, many=True)
    class Meta:
        model = Event
        fields = ('url', 'id', 'name', 'owner', 'created_at', 'updated_at', 'participants',)

    def create(self, validated_data):
        #participant_data = validated_data.pop('participants')
        event = Event.objects.create(**validated_data)
        Membership.objects.create(person=event.owner, event=event)
        return event

