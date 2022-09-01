from django.urls import path, include
from user.views import RegistrationAPIView, UserPageAPIView, RegistrationSuperUserAPIView
from rest_framework import routers

urlpatterns = [
    path("registration/", RegistrationAPIView.as_view(), name="registration"),
    path("authentication/", include("rest_framework.urls"), name="authentication"),
    path("user_page/<str:email>/", UserPageAPIView.as_view(), name="user_page"),
    path('create_superuser/', RegistrationSuperUserAPIView.as_view(), name="create_superuser"),
    # path('user_page/<str:email>', UserPageView.as_view(), name='user_page'),
    # path('help', HelpUserView.as_view(), name='help'),
]
