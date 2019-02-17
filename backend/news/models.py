import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse
from django.utils import timezone

from DSMS.utils import unique_slug_generator

User = get_user_model()


class Category(models.Model):
    """Категории"""
    name = models.CharField("Название", max_length=100)
    parent = models.ForeignKey(
        'self',
        verbose_name="Род. категория",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    slug = models.SlugField("url", max_length=100, unique=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("news:post_list", kwargs={"slug": self.slug})


class Tags(models.Model):
    """Теги"""
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("url", max_length=100, unique=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name


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

    category = models.ManyToManyField(Category, verbose_name="Категория")
    tag = models.ManyToManyField(Tags, verbose_name="Теги")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "news:post_detail",
            kwargs={
                 "category": self.category.first().slug,
                 "slug": self.slug
            }
        )

    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(self, self.title)
        super(Post, self).save(*args, **kwargs)
