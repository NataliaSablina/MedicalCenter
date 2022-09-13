from django.urls import path, include
from user.views import (
    RegistrationAPIView,
    UserPageAPIView,
    RegistrationSuperUserAPIView,
    UpdateUserAPIView,
    UpdateSuperUserAPIView,
    DeleteUserAPIView, HelpUserView,
)
from rest_framework import routers

urlpatterns = [
    path("registration/", RegistrationAPIView.as_view(), name="registration"),
    path("authentication/", include("rest_framework.urls"), name="authentication"),
    path("user_page/<str:email>/", UserPageAPIView.as_view(), name="user_page"),
    path(
        "create_superuser/",
        RegistrationSuperUserAPIView.as_view(),
        name="create_superuser",
    ),
    path("update_user/<str:email>/", UpdateUserAPIView.as_view(), name="update_user"),
    path(
        "update_superuser/<str:email>/",
        UpdateSuperUserAPIView.as_view(),
        name="update_superuser",
    ),
    path("delete_user/<str:email>/", DeleteUserAPIView.as_view(), name="delete_user"),
    # path('user_page/<str:email>', UserPageView.as_view(), name='user_page'),
    path('help/', HelpUserView.as_view(), name='help'),
]
