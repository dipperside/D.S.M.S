from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class LandingPage(models.Model):
    """Lending"""
    title = models.CharField("Заголовок", max_length=500)
    page = RichTextUploadingField()
    # style = models.FileField(upload_to="")

    class Meta:
        verbose_name = "Главная"
        verbose_name_plural = "Главная"

    def __str__(self):
        return self.title



