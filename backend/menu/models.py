from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    """Меню"""
    name = models.CharField("Название", max_length=100)
    slug = models.CharField("Название на лат.", max_length=100)
    status = models.BooleanField("Только для зарегистрированных", default=False)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name


class MenuItem(MPTTModel):
    """Пункты меню"""
    name = models.CharField("Название на лат.", max_length=100)
    title = models.CharField("Название пункта на сате", max_length=100)
    parent = TreeForeignKey(
        'self',
        verbose_name="Род. пункт меню",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )
    menu = models.ForeignKey(Menu, verbose_name="Меню", on_delete=models.CASCADE)
    status = models.BooleanField("Только для зарегистрированных", default=False)
    url = models.CharField("Ссылка на внешний ресурс", max_length=100, null=True, blank=True)
    link = models.SlugField("URL", unique=True, max_length=500, null=True, blank=True)

    content_type = models.ForeignKey(
        ContentType,
        verbose_name="Ссылка на: ",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    object_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        return self.name





