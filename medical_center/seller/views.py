from rest_framework import generics

from seller.models import Seller
from seller.serializers import SellerSerializer


class SellerListAPIView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        email = self.kwargs.get("email", None)
        if not email:
            return Seller.objects.all()
        return Seller.objects.filter(user__email=email)
