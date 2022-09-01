from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from rest_framework import status, generics
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from medical_center import settings
from user.forms import HelpUserForm
from user.models import MyUser
from user.serializers import (
    RegistrationSerializer,
    UserSerializer,
    RegistrationSuperUserSerializer,
)


class RegistrationAPIView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["response"] = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserPageAPIView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        email = self.kwargs.get("email")
        return MyUser.objects.filter(email=email)


class RegistrationSuperUserAPIView(generics.CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegistrationSuperUserSerializer
    permission_classes = [IsAdminUser]


# class UserPageView(View):
#     def get(self, request, email):
#         user = MyUser.objects.get(email=email)
#         context = {
#             "user": user,
#         }
#         return render(request, "user/user_page.html", context)
#
#
# class HelpUserView(LoginRequiredMixin, View):
#     login_url = "authentication"
#
#     def get(self, request):
#         help_user_form = HelpUserForm()
#         context = {
#             "form": help_user_form,
#         }
#         return render(request, "user/help_user_form.html", context)
#
#     def post(self, request):
#         help_user_form = HelpUserForm(request.POST)
#         if help_user_form.is_valid():
#             subject = "Help for client"
#             from_email = help_user_form.cleaned_data["email"]
#             message = help_user_form.cleaned_data["message"]
#             if from_email == request.user.email:
#                 try:
#                     send_mail(
#                         subject,
#                         message,
#                         from_email,
#                         [settings.EMAIL_HOST_USER],
#                         fail_silently=False,
#                     )
#                     messages.error(request, "Mail is sent successful")
#                 except BadHeaderError:
#                     messages.error(request, "Send email wrong")
#                     return redirect("help")
#                 return redirect("home_page")
#             else:
#                 messages.error(request, "Your email is wrong")
#         return redirect("help")
