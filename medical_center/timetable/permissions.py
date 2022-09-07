from rest_framework import permissions
from doctors.models import Doctor


class IsAdminAndDoctorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return request.user and request.user.is_staff
        else:
            try:
                doctor = Doctor.objects.get(user=request.user)
                return request.user and doctor.is_doctor
            except:
                return False
