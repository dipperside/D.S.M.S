from django.shortcuts import render
from django.views.generic.base import View

from .models import LandingPage


class HomePage(View):
    """Вывод главной страницы"""
    def get(self, request):
        return render(request, "landing/index.html", {"home": LandingPage.objects.first()})
