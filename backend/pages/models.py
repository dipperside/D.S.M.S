from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Pages(models.Model):
    """Страницы"""
    title = models.CharField("Заголовок", max_length=500)
    text = RichTextUploadingField()
    template = models.CharField("Шаблон", max_length=500, default="pages/index.html")
    slug = models.SlugField("URL", max_length=500, default="")
    activate = models.BooleanField("Опубликовать?", default=True)

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"

    def __str__(self):
        return self.title



