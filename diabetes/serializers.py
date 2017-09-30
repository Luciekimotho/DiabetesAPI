from rest_framework import serializers
from .models import Profile
from .models import Reading

class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = '__all__'


class ReadingSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reading
        fields = '__all__'


class UserInlineSerializer(serializers.ModelSerializer):
    readings = ReadingSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('user', 'readings')