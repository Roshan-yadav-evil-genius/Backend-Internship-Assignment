from rest_framework import serializers
from .models import Event 

from rest_framework import serializers

class CommaSeparatedField(serializers.CharField):
    def to_representation(self, value):
        if isinstance(value,list):
            return value
        return value.split(',') if value else []

    def to_internal_value(self, data):
        # return ','.join(data) if data else ''
        if isinstance(data,list):
            return data
        else:
            data=data.strip("[").strip("]").replace("'","")
        return data

class EventSerializer(serializers.ModelSerializer):
    attendees=CommaSeparatedField()

    class Meta:
        model= Event
        fields="__all__"

class EventRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        exclude=["id"]