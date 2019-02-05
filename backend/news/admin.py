from django.contrib import admin

from backend.news.models import Post
from backend.news.forms import PostAdminForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Новость"""
    model = Post
    form = PostAdminForm
    
    list_display = ["title", "author", "created", "published", "id"]
    list_editable = ["published", ]
    search_fields = ["title", ]
    list_filter = ["author", "published", ]
