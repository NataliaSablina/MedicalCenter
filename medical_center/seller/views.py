from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from seller.models import Seller, CommentSeller
from seller.permissions import IsOwnerSellerOrAdminOrReadOnly
from seller.serializers import (
    SellerSerializer,
    RegistrationSellerSerializer,
    CommentSellerSerializer,
    SellerUpdateSerializer,
)


class SellerListAPIView(generics.ListAPIView):
    serializer_class = SellerSerializer

    def get_queryset(self):
        email = self.kwargs.get("email", None)
        queryset = Seller.objects.select_related("user").filter(user__email=email)
        if not email:
            return Seller.objects.all()
        return queryset


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
        email = self.kwargs.get(self.lookup_url_kwarg)
        if not email:
            return CommentSeller.objects.all()
        return CommentSeller.objects.filter(seller__user__email=email)


class UpdateSellerAPIView(generics.RetrieveUpdateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerUpdateSerializer
    lookup_url_kwarg = "email"
    permission_classes = [IsOwnerSellerOrAdminOrReadOnly]

    def get_object(self):
        email = self.kwargs.get(self.lookup_url_kwarg)
        instance = (
            Seller.objects.select_related("user")
            .prefetch_related("timetable")
            .filter(user__email=email)
            .first()
        )
        if not instance:
            raise NotFound
        return instance

    def put(self, request, *args, **kwargs):
        seller = Seller.objects.select_related("user").get(
            user__email=kwargs.get("email", None)
        )
        serializer = SellerUpdateSerializer(instance=seller, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer.save()
        return Response({"post": serializer.data})
