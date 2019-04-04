from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin
# from django.urls import reverse
# from django.utils.html import format_html
# from .models import Profile
#
# User = get_user_model()
#
#
# # class UserProfileInline(admin.StackedInline):
# #     model = Profile
# #     verbose_name_plural = 'Профили'
#
#
# # class NewUserAdmin(admin.ModelAdmin):
# class NewUserAdmin(UserAdmin):
#     # inlines = (UserProfileInline, )
#     model = Profile
#     list_display = (
#         "username",
#         "is_active",
#         "email",
#         "first_name",
#         "last_name",
#         "permalink",
#         "is_superuser",
#         "is_staff",
#     )
#
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(NewUserAdmin, self).get_inline_instances(request, obj)
#
#
#     # 'View on site' didn't work since the original User model needs to
#     # have get_absolute_url defined. So showing on the list display
#     # was a workaround.
#     def permalink(self, obj):
#         url = reverse("profiles:show", kwargs={"slug": obj.profile.slug})
#         # Unicode hex b6 is the Pilcrow sign
#         return format_html('<a href="{}">{}</a>'.format(url, "\xb6"))
#
#
# admin.site.unregister(User)
# admin.site.register(User, NewUserAdmin)
