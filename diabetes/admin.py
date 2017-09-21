from django.contrib import admin

# Register your models here.
from .models import Profile, Readings

admin.site.register(Profile)
admin.site.register(Readings)

