from django.contrib import admin
from doctors.models import DoctorsCategory, Doctor

admin.site.register(DoctorsCategory)
admin.site.register(Doctor)
