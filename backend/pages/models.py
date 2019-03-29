from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Pages(models.Model):
    """Страницы"""
    title = models.CharField("Заголовок", max_length=500)
    text = RichTextUploadingField()
    template = models.CharField("Шаблон", max_length=500, default="pages/index.html")
    slug = models.SlugField("URL", max_length=500, default="", null=True, blank=True)
    activate = models.BooleanField("Опубликовать?", default=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.slug:
            return reverse("page", kwargs={"slug": self.slug})
        else:
            return reverse("page")


class PageHit(models.Model):
    """page hit"""
    url = models.CharField("URL", max_length=300)
    hit_count = models.PositiveIntegerField("Визиты", default=0)

    class Meta:
        verbose_name = "Визит страницы"
        verbose_name_plural = "Визиты страницы"
