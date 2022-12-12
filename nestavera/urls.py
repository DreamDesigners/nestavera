from django.contrib import admin
from django.urls import path
from category.views import CategoriesListView, TagsListView
from article.views import ArticlesListView, ArticleDetailView
from contact.views import ContactsCreateView
from career.views import JobsListView, JobCategoryListView, JobLocationListView, JobApplicationCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', CategoriesListView.as_view(), name='categories-list'),
    path('tags/', TagsListView.as_view(), name='tags-list'),
    path('articles/', ArticlesListView.as_view(), name='articles-list'),
    path('articles/category/<slug:category>/', ArticlesListView.as_view(), name='articles-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('careers/', JobsListView.as_view(), name='jobs'),
    path('careers-categories/', JobCategoryListView.as_view(), name='jobs-categories'),
    path('careers-locations/', JobLocationListView.as_view(), name='jobs-locations'),
    path('contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('job_application/', JobApplicationCreateView.as_view(), name='job_application'),
]


urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
