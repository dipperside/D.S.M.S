from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.views.generic.base import View

from .models import Post


class PostList(View):
    """Вывод списка новостей"""
    def get(self, request):
        try:
            a = Post.objects.filter(sites__id=get_current_site(request).id)
        except Post.DoesNotExist:
            raise Http404("Article does not exist on this site")
        return HttpResponse(a)
