from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Menu, MenuItem


@admin.register(Menu)
class Menu(admin.ModelAdmin):
    """Меню"""
    list_display = ("name", "slug", "status", "id")


@admin.register(MenuItem)
class MenuItemAdmin(MPTTModelAdmin):
    """Пункты меню"""
    mptt_level_indent = 20
