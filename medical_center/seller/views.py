from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from seller.models import Seller
from seller.serializers import SellerSerializer, RegistrationSellerSerializer


class SellerListAPIView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        email = self.kwargs.get("email", None)
        if not email:
            return Seller.objects.all()
        return Seller.objects.filter(user__email=email)


class RegistrationSellerAPIView(generics.CreateAPIView):
    queryset = Seller
    serializer_class = RegistrationSellerSerializer
    permission_classes = [IsAdminUser]
