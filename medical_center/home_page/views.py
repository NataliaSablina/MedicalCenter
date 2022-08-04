from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View


class HomePageView(LoginRequiredMixin, View):
    login_url = 'authentication'

    def get(self, request):
        return render(request, 'home_page/home_page.html')


