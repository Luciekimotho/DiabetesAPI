from django.contrib import admin

# Register your models here.
from .models import Profile, Reading

admin.site.register(Profile)
admin.site.register(Reading)

