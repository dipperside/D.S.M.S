from django.urls import path

from .views import *

urlpatterns = [
    path('', Comment.as_view(), name="comments")
]
