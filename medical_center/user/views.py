from django import views
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from medical_center import settings
from .forms import RegistrationForm, AuthenticationForm, HelpUserForm
from .models import MyUser
from .serializers import RegistrationSerializer


class RegistrationAPIView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = serializer.data
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)

    # Добавляем права доступа
# class UserRegistrationView(View):
#     def get(self, request):
#         registration_form = RegistrationForm()
#         context = {
#             'form': registration_form,
#         }
#         return render(request, 'user/registration_form.html', context)
#
#     def post(self, request):
#         registration_form = RegistrationForm(request.POST)
#         if registration_form.is_valid():
#             user = registration_form.save()
#             login(request, user)
#             return redirect('user_page', user.email)
#         else:
#             for field, errors in registration_form.errors.items():
#                 messages.error(request, errors)
#             return redirect('registration')


class UserAuthenticationView(View):
    def get(self, request):
        authentication_form = AuthenticationForm()
        context = {
            'form': authentication_form,
        }
        return render(request, 'user/authentication_form.html', context)

    def post(self, request):
        authentication_form = AuthenticationForm(request.POST)
        if authentication_form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('user_page', user.email)
            else:
                messages.error(request, "You entered wrong email or password")
                return redirect('authentication')
        else:
            for field, errors in authentication_form.errors.items():
                messages.error(request, errors)
            return redirect('authentication')


class UserPageView(View):
    def get(self, request, email):
        user = MyUser.objects.get(email=email)
        context = {
            'user': user,
        }
        return render(request, 'user/user_page.html', context)


class HelpUserView(LoginRequiredMixin, View):
    login_url = 'authentication'

    def get(self, request):
        help_user_form = HelpUserForm()
        context = {
            "form": help_user_form,
        }
        return render(request, "user/help_user_form.html", context)

    def post(self, request):
        help_user_form = HelpUserForm(request.POST)
        if help_user_form.is_valid():
            subject = "Help for client"
            from_email = help_user_form.cleaned_data["email"]
            message = help_user_form.cleaned_data["message"]
            if from_email == request.user.email:
                try:
                    send_mail(subject, message, from_email, [settings.EMAIL_HOST_USER], fail_silently=False)
                    messages.error(request, 'Mail is sent successful')
                except BadHeaderError:
                    messages.error(request, 'Send email wrong')
                    return redirect('help')
                return redirect('home_page')
            else:
                messages.error(request, 'Your email is wrong')
        return redirect('help')
