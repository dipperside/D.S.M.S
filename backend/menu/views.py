from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.views.generic.base import View

from .models import MenuItem


class LinkMenu(View):
    """Переход по ссылке"""
    def get(self, request, slug):
        item = MenuItem.objects.get(link=slug)
        print(ContentType.objects.get_for_model(item))
