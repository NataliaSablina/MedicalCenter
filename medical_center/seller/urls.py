from django.urls import path, include

from seller.views import SellerListAPIView, RegistrationSellerAPIView

urlpatterns = [
    path("all/sellers/", SellerListAPIView.as_view(), name="all-sellers"),
    path("seller/<str:email>/", SellerListAPIView.as_view(), name="seller"),
    path("create_seller/", RegistrationSellerAPIView.as_view(), name="create_seller"),
]
