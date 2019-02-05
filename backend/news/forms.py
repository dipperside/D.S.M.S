from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from backend.news.models import Post


class PostAdminForm(forms.ModelForm):
    """Форма новости"""
    content = forms.CharField(widget=CKEditorUploadingWidget(), label="Контент")

    class Meta:
        model = Post
        fields = '__all__'
