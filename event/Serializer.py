from rest_framework import serializers
from .models import Event ,Category,Subcategory 
from django.contrib.auth.models import User 

from rest_framework import serializers

class CommaSeparatedField(serializers.CharField):
    def to_representation(self, value):
        return value.split(',') if value else []

    def to_internal_value(self, data):
        # return ','.join(data) if data else ''
        data=data.strip("[").strip("]").replace("'","")
        return data

class UserFullNameField(serializers.RelatedField):
    def to_representation(self, value):
        return f"{value.username}"
    
    def to_internal_value(self, data):
        
        user = User.objects.get(username=data)
        return user

    
class EventSerializer(serializers.ModelSerializer):
    Category=serializers.SlugRelatedField(slug_field="name",queryset=Category.objects.all(),many=False)   
    Subcategory=serializers.SlugRelatedField(slug_field="name",queryset=Subcategory.objects.all(),many=False)
    attendees=CommaSeparatedField()
    user = UserFullNameField(queryset=User.objects.all())

    class Meta:
        model= Event
        fields="__all__"
    
    def get_user(self,obj):
        return obj.user.get_full_name()
    
    # def get_Category(self,obj):
    #     return obj.Category.name

    # def get_Subcategory(self,obj):
    #     return obj.Subcategory.name

    # def get_attendees(self,obj):
    #     return obj.attendees.split(",")

class EventRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model= Event
        exclude=["id"]