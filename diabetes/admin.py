from django.contrib import admin

# Register your models here.
from .models import Profile, Reading, Doctor, Caregiver

admin.site.register(Profile)
admin.site.register(Reading)
admin.site.register(Doctor)
admin.site.register(Caregiver)

