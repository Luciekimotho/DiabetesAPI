from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

class Caregiver(models.Model):
	name = models.OneToOneField(User, on_delete=models.CASCADE)
	relation = models.CharField(max_length = 20)
	phone = models.CharField(max_length = 20)
	
	def publish(self):
		self.save()
	
	def __str__(self):
		return str(self.name)

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="patient_name")
	dateOfBirth = models.DateTimeField()
	height = models.IntegerField()
	weight = models.IntegerField()
	location = models.CharField(max_length = 200)
	caregiver = models.ForeignKey(Caregiver,blank = True, null=True, related_name='patients', on_delete=models.CASCADE)

	MALE = "MALE"
	FEMALE = "FEMALE"

	SEX_CHOICES = (
	    (MALE, "Male"),
	    (FEMALE, "Female"),
	    
	)
	sex= models.CharField(choices=SEX_CHOICES,
					max_length = 10)

	def __str__(self):
		return str(self.user)

class Reading(models.Model):
	user = models.ForeignKey(User,related_name='readings', on_delete=models.CASCADE)
	glucoseLevel = models.DecimalField(max_digits=7, decimal_places=4)
	timePeriod = models.CharField(max_length = 50)
	timeOfDay = models.DateTimeField(auto_now=True)
	action = models.CharField(max_length = 200)
	medication= models.CharField(max_length = 200)
	notes= models.CharField(max_length = 500)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.glucoseLevel


class Doctor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length = 20)	
	notes = models.CharField(max_length = 1000)
	patients = models.ManyToManyField(Profile, related_name='doctors',blank = True)
	def __str__(self):
		return str(doctor.user)

class Reminder(models.Model):
	reminder = models.CharField(max_length = 50)
	user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
	time = models.DateTimeField(auto_now=True)
	alarm = models.BooleanField(default=True)

	def __str__(self):
		return str(self.reminder) 