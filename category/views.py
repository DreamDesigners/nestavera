from rest_framework import generics
from category.models import Category, CategorySerializer
from url_filter.integrations.drf import DjangoFilterBackend


class CategoriesListView(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  filter_backends = (DjangoFilterBackend,)