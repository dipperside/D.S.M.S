import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BaseProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField(
        "Аватар", upload_to="profile_pics/%Y-%m-%d/", null=True, blank=True
    )
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)

    class Meta:
        abstract = True


class Profile(BaseProfile):
    def __str__(self):
        return self.user.username
