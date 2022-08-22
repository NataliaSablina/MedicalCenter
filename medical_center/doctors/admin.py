from django.contrib import admin
from doctors.models import DoctorsCategory, Doctor, CommentDoctor

admin.site.register(DoctorsCategory)
admin.site.register(Doctor)
admin.site.register(CommentDoctor)
