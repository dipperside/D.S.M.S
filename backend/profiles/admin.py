from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.html import format_html
from .models import Profile

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = Profile


class NewUserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]
    list_display = (
        # "id",
        "username",
        "is_active",
        "email",
        "first_name",
        "last_name",
        "permalink",
        "is_superuser",
        "is_staff",
    )

    # 'View on site' didn't work since the original User model needs to
    # have get_absolute_url defined. So showing on the list display
    # was a workaround.
    def permalink(self, obj):
        url = reverse("profiles:show", kwargs={"slug": obj.profile.slug})
        # Unicode hex b6 is the Pilcrow sign
        return format_html('<a href="{}">{}</a>'.format(url, "\xb6"))


admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
