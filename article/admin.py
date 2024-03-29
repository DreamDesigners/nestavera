from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from article.models import Article

class ArticleAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Article
        fields = ["cover", "category", "title", "slug", "short_body", "external_link", "body", "tags", "is_featured", "is_active"]

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ["title", "category", "is_featured", "is_active", "updated_at"]
    list_editable = ["is_featured", "is_active"]
    list_filter = ["is_featured", "is_active"]
    search_fields = ["title", "short_body", "body"]
    prepopulated_fields = {"slug": ("title",),}
    save_as = True

admin.site.register(Article, ArticleAdmin)