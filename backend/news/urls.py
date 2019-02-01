from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from .views import *

app_name = 'news'

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('<slug>', PostDetailView.as_view(), name="post_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)