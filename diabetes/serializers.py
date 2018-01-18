from rest_framework import serializers
from .models import Profile, Doctor, Caregiver, Reminder
from .models import Reading
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


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

class DoctorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Doctor
        fields = '__all__'

class CaregiverSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Caregiver
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reminder
        fields = '__all__'