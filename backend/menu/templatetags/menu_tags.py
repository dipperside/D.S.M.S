from django import template

from backend.menu.models import MenuItem


register = template.Library()


@register.inclusion_tag("menu/menu-item.html")
def menu_item(menu):
    """Вывод меню"""
    return {"items": MenuItem.objects.filter(menu__slug=menu, parent__isnull=True)}
    # return {"items": MenuItem.objects.all()}
