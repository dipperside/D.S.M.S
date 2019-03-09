from django.urls import path

from .views import *

app_name = 'news'

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('<slug:slug>/', PostList.as_view(), name="post_list"),
    path('<slug:category>/<slug:slug>/', PostDetailView.as_view(), name="post_detail"),
]
