from django.contrib import admin

# Register your models here.
from .models import Profile, Reading, Doctor, Caregiver, Reminder

admin.site.register(Profile)
admin.site.register(Reading)
admin.site.register(Doctor)
admin.site.register(Caregiver)
admin.site.register(Reminder)

