from django.urls import path, include
from user.views import UserPageView, HelpUserView, RegistrationAPIView
from rest_framework import routers

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('authentication/', include('rest_framework.urls'), name='authentication'),
    # path('user_page/<str:email>', UserPageView.as_view(), name='user_page'),
    # path('help', HelpUserView.as_view(), name='help'),
]
