from rest_framework import serializers
from .models import Event

from rest_framework import serializers

class ListField(serializers.Field):
    def to_representation(self, value):
        return value.split(',') if value else []

    def to_internal_value(self, data):
        return ','.join(data) if data else ''
    
class EventSerializer(serializers.ModelSerializer):
    Category=serializers.SerializerMethodField()
    Subcategory=serializers.SerializerMethodField()
    attendees=serializers.SerializerMethodField()
    user=serializers.SerializerMethodField()

    class Meta:
        model= Event
        exclude=["id"]
    
    def get_user(self,obj):
        return obj.user.get_full_name()
    
    def get_Category(self,obj):
        return obj.Category.name

    def get_Subcategory(self,obj):
        return obj.Subcategory.name

    def get_attendees(self,obj):
        return obj.attendees.split(",")

class EventRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        exclude=["id"]