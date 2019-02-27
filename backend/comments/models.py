from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()

# Create your models here.


class Comment(models.Model):
    """ Комменты"""
    author = models.OneToOneField(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        null=True)
    news = models.OneToOneField(
        'news.Post',
        verbose_name="Новость",
        on_delete=models.CASCADE
    )
    comment = RichTextField("Комментарий", default="")
    parent = models.ForeignKey(
        'self',
        verbose_name="Род. категория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created = models.DateTimeField("Создан", auto_now_add=True)
    updated = models.DateTimeField("Обновлен", default=timezone.now)
