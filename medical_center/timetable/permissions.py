from rest_framework import permissions

from doctors.models import Doctor


class IsAdminAndDoctorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):  # права на уровне запроса
        if request.method in permissions.SAFE_METHODS:  # запросы только для чтения данных
            return True
        if request.user.is_staff:
            return request.user and request.user.is_staff
        else:
            try:
                doctor = Doctor.objects.get(user=request.user)
                return request.user and doctor.is_doctor
            finally:
                return False
