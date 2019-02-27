from django.contrib import admin

# Register your models here.
from backend.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "post", "message", "reply")