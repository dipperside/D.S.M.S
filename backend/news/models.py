import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse
from django.utils import timezone

from DSMS.utils import unique_slug_generator

User = get_user_model()


class Post(models.Model):
    """Новость"""
    author = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.SET_NULL,
        null=True)
    title = models.CharField("Заголовок", max_length=150)
    slug = models.SlugField("Слаг", max_length=150, unique=True, default=uuid.uuid4)
    thumbnail = models.ImageField("Риссунок", upload_to='posts/%Y/%m/%d', blank=True)
    published = models.BooleanField("Опубликовано", default=False)
    created = models.DateTimeField("Создана", auto_now_add=True)
    modified = models.DateTimeField("Обновлена", default=timezone.now)
    sites = models.ManyToManyField(Site, verbose_name="Сайт")
    content = RichTextUploadingField("Контент", default="")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news:post_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.title)
        super(Post, self).save(*args, **kwargs)
