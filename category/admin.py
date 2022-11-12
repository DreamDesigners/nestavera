from django.contrib import admin
from category.models import Category, Tag


admin.site.site_header = "Nestavera"
admin.site.site_title = "Nestavera"


class CategoryAdmin(admin.ModelAdmin):
  list_display = ["parent", "title", "slug", "is_active", "updated_at"]
  list_display_links = ["title"]
  list_editable = ["parent", "is_active"]
  list_filter = ["is_active"]
  search_fields = ["title"]
  prepopulated_fields = {"slug": ("title",),}

  class Meta:
    model = Category


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)