from rest_framework.serializers import ModelSerializer
from core.models import Events

class EventsSerializer(ModelSerializer):
    class Meta:
        model = Events
        fields = ['*']
