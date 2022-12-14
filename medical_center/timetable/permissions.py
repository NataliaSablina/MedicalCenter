from rest_framework import permissions
from doctors.models import Doctor
from seller.models import Seller


class IsAdminDoctorSellerOrReadOnly(permissions.BasePermission):
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
                try:
                    seller = Seller.objects.get(user=request.user)
                    return request.user and seller.is_seller
                except:
                    return False
