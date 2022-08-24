from rest_framework import generics

from seller.models import Seller
from seller.serializers import SellerSerializer


class SellerListAPIView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk", None)
        if not pk:
            return Seller.objects.all()
        return Seller.objects.filter(pk=pk)


