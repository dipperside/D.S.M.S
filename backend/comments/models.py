from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.utils import timezone


# Create your models here.

class Comment(models.Model):
    """ Комментарий """
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        null=True)
    post = models.ForeignKey("news.Post", verbose_name="Новость", on_delete=models.CASCADE)
    message = TextField("Сообщение", default="")
    created = models.DateTimeField("Создан", auto_now_add=True)
    updated = models.DateTimeField("Обновлен", default=timezone.now)
    reply = models.ForeignKey(
        "self",
        verbose_name="Коммент",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Комментарий",
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f"{self.id}-{self.author}"

    def get_absolute_url(self):
        # from django.core.urlresolvers import reverse
        return reverse('people.views.details', args=[str(self.id)])