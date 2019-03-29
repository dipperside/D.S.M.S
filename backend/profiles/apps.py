# from __future__ import unicode_literals
from django.apps import AppConfig


class ProfileConfig(AppConfig):
    name = "backend.profiles"
    verbose_name = "Профиль юзера"

    def ready(self):
        from . import signals  # noqa
