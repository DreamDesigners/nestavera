from rest_framework import generics
from category.models import Category, CategorySerializer, Tag, TagsSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class CategoriesListView(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  filter_backends = (DjangoFilterBackend,)


class TagsListView(generics.ListAPIView):
  queryset = Tag.objects.filter(is_active=True)
  serializer_class = TagsSerializer
  pagination_class = None
  filter_backends = (DjangoFilterBackend,)