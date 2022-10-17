from rest_framework import generics
from article.models import Article, ArticleSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class ArticlesListView(generics.ListAPIView):
  queryset = Article.objects.all()
  serializer_class = ArticleSerializer
  filter_backends = (DjangoFilterBackend,)