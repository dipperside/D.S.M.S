from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models


class Post(models.Model):
    """Новость"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.SET_NULL, null=True)
    title = models.CharField("Заголовок", max_length=150)
    text = models.TextField("Текст статьи")
    date = models.DateTimeField("Дата", auto_now_add=True)
    sites = models.ManyToManyField(Site)


    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title