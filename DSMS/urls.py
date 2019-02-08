"""DSMS
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from jet_django.urls import jet_urls


urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('jet_api/', include(jet_urls)),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('news/', include('backend.news.urls')),
    path('', include('backend.pages.urls')),
    # path('', include('backend.menu.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
