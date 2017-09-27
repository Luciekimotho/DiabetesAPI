from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.CharField(max_length = 200)
	dateOfBirth = models.DateTimeField()
	height = models.IntegerField()
	weight = models.IntegerField()
	location = models.CharField(max_length = 200)

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

	# @receiver(post_save, sender=User)
	# def create_user_profile(sender, instance, created, **kwargs):
	#     if created:
	#         Profile.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def save_user_profile(sender, instance, **kwargs):
	#     instance.profile.save()

class Readings(models.Model):
	user = models.ForeignKey(Profile,related_name='readings', on_delete=models.CASCADE)
	glucoseLevel = models.DecimalField(max_digits=7, decimal_places=4)
	timePeriod = models.CharField(max_length = 50)
	timeOfDay = models.DateTimeField(auto_now=True)
	action = models.CharField(max_length = 200)
	medication= models.CharField(max_length = 200)
	notes= models.CharField(max_length = 500)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	# def __str__(self):
	# 	return self.glucoseLevel
		
