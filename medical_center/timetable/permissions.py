from rest_framework import permissions

from doctors.models import Doctor


class IsAdminAndDoctorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):  # права на уровне запроса
        if request.method in permissions.SAFE_METHODS: # запросы только для чтения данных
            return True
        doctor = Doctor.objects.get(user=request.user)
        print(doctor)
        return bool((request.user and doctor.is_doctor) or (request.user and request.user.is_staff))

    def has_object_permission(self, request, view, obj):
        print(obj)