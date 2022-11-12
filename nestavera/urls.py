from django.contrib import admin
from django.urls import path
from category.views import CategoriesListView, TagsListView
from article.views import ArticlesListView, ArticleDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', CategoriesListView.as_view(), name='categories-list'),
    path('tags/', TagsListView.as_view(), name='tags-list'),
    path('articles/', ArticlesListView.as_view(), name='articles-list'),
    path('articles/category/<slug:category>/', ArticlesListView.as_view(), name='articles-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail')
]


urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
