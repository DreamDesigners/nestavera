from rest_framework import generics
from category.models import Category, CategorySerializer, Tag, TagsSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class CategoriesListView(generics.ListAPIView):
  queryset = Category.objects.filter(parent__isnull=False)
  serializer_class = CategorySerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = '__all__'


class TagsListView(generics.ListAPIView):
  queryset = Tag.objects.filter(is_active=True)
  serializer_class = TagsSerializer
  pagination_class = None
  filter_backends = (DjangoFilterBackend,)
  filter_fields = '__all__'