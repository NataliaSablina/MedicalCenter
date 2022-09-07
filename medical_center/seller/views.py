from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from seller.models import Seller, CommentSeller
from seller.serializers import (
    SellerSerializer,
    RegistrationSellerSerializer,
    CommentSellerSerializer,
)


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


class CreateCommentSellerAPIView(generics.CreateAPIView):
    queryset = CommentSeller.objects.all()
    serializer_class = CommentSellerSerializer


class UpdateCommentSellerAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSellerSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "title"

    def get_queryset(self):
        title = self.kwargs.get("title")
        if not title:
            return CommentSeller.objects.all()
        return CommentSeller.objects.filter(title=title)


class SellerCommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSellerSerializer
    lookup_url_kwarg = "email"

    def get_queryset(self):
        title = self.kwargs.get(self.lookup_url_kwarg)
        if not title:
            return CommentSeller.objects.all()
        return CommentSeller.objects.filter(seller__user__email=title)
