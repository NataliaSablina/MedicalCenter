from django.urls import path, include

from seller.views import SellerListAPIView, RegistrationSellerAPIView, CreateCommentSellerAPIView, \
    UpdateCommentSellerAPIView, SellerCommentListAPIView

urlpatterns = [
    path("all/sellers/", SellerListAPIView.as_view(), name="all-sellers"),
    path("seller/<str:email>/", SellerListAPIView.as_view(), name="seller"),
    path("create_seller/", RegistrationSellerAPIView.as_view(), name="create_seller"),
    path("create_comment_seller/", CreateCommentSellerAPIView.as_view(), name="create_comment_seller"),
    path("update_comment_seller/<str:title>/", UpdateCommentSellerAPIView.as_view(), name="update_comment_seller"),
    path("comments_seller/<str:email>/", SellerCommentListAPIView.as_view(), name="comments_seller"),
]
