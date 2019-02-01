from django.contrib import admin

from .models import Pages


class PagesAdmin(admin.ModelAdmin):
    """Статичные страницы"""
    list_display = ("title", "activate")
    list_editable = ("activate", )
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Pages, PagesAdmin)
