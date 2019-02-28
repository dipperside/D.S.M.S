from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *

app_name = 'news'

urlpatterns = [
    path('<slug:slug>/', PostList.as_view(), name="post_list"),
    path('<slug:category>/<slug:slug>/', PostDetailView.as_view(), name="post_detail"),
    path('comments/<slug:category>/<slug:slug>/', AddComment.as_view(), name="add_comment"),
]