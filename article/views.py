from rest_framework import generics
from article.models import Article, ArticleListSerializer, ArticleDetailSerializer
from url_filter.integrations.drf import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status


class ArticlesListView(generics.ListAPIView):
  serializer_class = ArticleListSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = '__all__'

  def get_queryset(self):
    if self.kwargs.get("category"):
      return Article.objects.filter(is_active=True, category__parent__slug=self.kwargs.get("category")).order_by('-updated_at')
    return Article.objects.filter(is_active=True).order_by('-updated_at')


class ArticleDetailView(generics.RetrieveAPIView):
  serializer_class = ArticleDetailSerializer

  def get_object(self):
    return Article.objects.get(id=self.kwargs.get("pk"))

  def get(self, request, *args, **kwargs):
    blog = self.get_object()
    serializer = ArticleListSerializer(
      Article.objects.filter(
        category=blog.category,
        tags__in=blog.tags.all()
      ).exclude(id=blog.id),
      many=True
    )

    return Response(
      status=status.HTTP_200_OK,
      data={
        "blog": ArticleDetailSerializer(blog).data,
        "related": serializer.data
      }
    )
