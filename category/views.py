from rest_framework import generics
from category.models import Category, CategorySerializer, Tag, TagsSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class CategoriesListView(generics.ListAPIView):
  queryset = Category.objects.filter(parent__isnull=False)
  serializer_class = CategorySerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = '__all__'

  def get_queryset(self):
    # get category from query params
    category = self.request.GET.get('parent_category', None)
    if category:
      return Category.objects.filter(parent__slug=category)
    return Category.objects.filter(parent__isnull=False)


class TagsListView(generics.ListAPIView):
  queryset = Tag.objects.filter(is_active=True)
  serializer_class = TagsSerializer
  pagination_class = None
  filter_backends = (DjangoFilterBackend,)
  filter_fields = '__all__'