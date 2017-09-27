from rest_framework import serializers
from .models import Profile
from .models import Readings

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = '__all__'


class ReadingsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Readings
        fields = ('glucoseLevel', 'timePeriod')


class UserReadingSerializer(serializers.ModelSerializer):
    readings = ReadingsSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('user', 'readings')