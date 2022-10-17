from django.db import models
from category.models import Category
from ckeditor.fields import RichTextField
from rest_framework import serializers


class Article(models.Model):
  category        = models.ForeignKey(Category, on_delete=models.CASCADE)
  title           = models.CharField(max_length=500)
  slug            = models.SlugField(max_length=500, unique=True)
  short_body      = models.TextField(max_length=1000)
  body            = RichTextField()

  is_featured   = models.BooleanField(default=False)
  is_active     = models.BooleanField(default=True)
  created_at    = models.DateTimeField(auto_now_add=True)
  updated_at    = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'