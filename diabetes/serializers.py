from rest_framework import serializers
from .models import Profile
from .models import Readings

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = '__all__'