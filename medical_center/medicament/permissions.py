from rest_framework import permissions

from seller.models import Seller


class IsAdminAndSellerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_staff:
            return request.user and request.user.is_staff
        else:
            try:
                seller = Seller.objects.get(user=request.user)
                return request.user and seller.is_seller
            except:
                return False


class IsOwnerSellerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.seller.user.email == request.user.email or request.user.is_staff
