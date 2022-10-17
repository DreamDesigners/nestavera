from django.contrib import admin
from django.urls import path
from category.views import CategoriesListView
from article.views import ArticlesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', CategoriesListView.as_view(), name='categories-list'),
    path('articles/', ArticlesListView.as_view(), name='articles-list')
]
