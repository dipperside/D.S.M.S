from django.contrib import admin

from backend.news.models import Post, Category, Tags
from backend.news.forms import PostAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категрии"""
    list_display = ("name", "id")
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    """Категрии"""
    list_display = ("name", "id")
    prepopulated_fields = {"slug": ("name", )}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Новость"""
    model = Post
    form = PostAdminForm
    
    list_display = ["title", "author", "created", "published", "id"]
    list_editable = ["published", ]
    search_fields = ["title", ]
    list_filter = ["author", "published", ]
