from django.urls import path

from .views import *

urlpatterns = [
    # path('<path:url>', Page.as_view(), name="page"),
    path('<slug:slug>/', Page.as_view(), name="page")
]