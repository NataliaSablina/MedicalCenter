from django.urls import path
from user.views import UserPageView, UserAuthenticationView, HelpUserView, RegistrationAPIView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('authentication/', UserAuthenticationView.as_view(), name='authentication'),
    path('user_page/<str:email>', UserPageView.as_view(), name='user_page'),
    path('help', HelpUserView.as_view(), name='help'),
]
