from django.urls import path, include

from seller.views import SellerListAPIView

urlpatterns = [
    path('all/sellers/', SellerListAPIView.as_view(), name='all-sellers'),
    path('seller/<int:pk>/', SellerListAPIView.as_view(), name='seller'),
]
