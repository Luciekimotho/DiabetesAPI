from rest_framework import serializers
from .models import Profile, Doctor, Caregiver, Reminder
from .models import Reading
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    # username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
    # password = serializers.CharField(min_length=8)

    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'], validated_data['email'],
    #          validated_data['password'])
    #     return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    
    class Meta: 
        model = Profile
        fields = ('user', 'dateOfBirth', 'height', 'weight', 'location', 'sex')
        
        def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            patient, created = Profile.objects.update_or_create(user=user,
             dateOfBirth = validated_data.pop('dateOfBirth'), 
             height = validated_data.pop('height'), weight = validated_data.pop('weight'),
             location = validated_data.pop('location'), sex=validated_data.pop('sex'))
            return patient

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
    user = UserSerializer(required=True)
    class Meta: 
        model = Doctor
        fields = ('user', 'phone', 'notes','patients')
        
        def create(self, validated_data):
            user_data = validated_data.pop('user')
            user = UserSerializer.create(UserSerializer(), validated_data=user_data)
            doctor, created = Doctor.objects.update_or_create(user=user,
             phone = validated_data.pop('phone'), 
             notes=validated_data.pop('notes'), patients=validated_data.pop('patients'))
            return doctor

class CaregiverSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Caregiver
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Reminder
        fields = '__all__'