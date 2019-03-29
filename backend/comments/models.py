from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from django.utils import timezone


class Comment(models.Model):
    """ Комментарий """
    author = models.ForeignKey(
        User,
        verbose_name="Автор",
        on_delete=models.CASCADE,
        null=True
    )
    post = models.ForeignKey(
        "news.Post",
        verbose_name="Новость",
        on_delete=models.CASCADE,
        related_name="comments"
    )
    message = models.TextField("Сообщение", default="")
    reply = models.ForeignKey(
        "self",
        verbose_name="Коммент",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='children',
    )
    created = models.DateTimeField("Создан", auto_now_add=True)
    updated = models.DateTimeField("Обновлен", default=timezone.now)
    moderated = models.BooleanField("Одобрен", default=False)

    class Meta:
        verbose_name = "Комментарий",
        verbose_name_plural = "Комментарии"
        ordering = ['id']

    def __str__(self):
        # return f"{self.id}-{self.author}"
        return f"{self.id}-{self.post} > {self.message[:20]}..."

    # def get_absolute_url(self):
    #     return reverse('news:add_comment', args=[str(self.id)])
