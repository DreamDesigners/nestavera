from django.db import models
from category.models import Category, Tag
from ckeditor.fields import RichTextField
from rest_framework import serializers
import os
import random
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.core.exceptions import ValidationError


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_file_path(instance, filename):
    new_filename = random.randint(1, 3231546414654785)
    name, ext =get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "resumes/{final_filename}".format(final_filename=final_filename)


class Article(models.Model):
  cover           = models.ImageField(upload_to=upload_file_path, blank=True, null=True)
  category        = models.ForeignKey(Category, on_delete=models.CASCADE, limit_choices_to={ "is_active": True, "parent__isnull": False })
  title           = models.CharField(max_length=500)
  slug            = models.SlugField(max_length=500, unique=True)
  short_body      = models.TextField(max_length=500, blank=True, null=True)
  body            = RichTextField(null=True, blank=True)
  external_link   = models.URLField(max_length=500, blank=True, null=True)

  is_featured   = models.BooleanField(default=False)
  is_active     = models.BooleanField(default=True)
  tags          = models.ManyToManyField(Tag, limit_choices_to={ "is_active": True })
  created_at    = models.DateTimeField(auto_now_add=True)
  updated_at    = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
  
  def clean(self):
    if not self.external_link:
      if not self.body or not self.short_body:
        raise ValidationError("Either external link or body is required")
    
  def save(self, *args, **kwargs):
    self.full_clean()
    super(Article, self).save(*args, **kwargs)

  
  class Meta:
      ordering = ['-updated_at']


class ArticleListSerializer(serializers.ModelSerializer):
    category_display = serializers.SerializerMethodField()
    cover = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            'id','title', 'short_body', 'external_link', 'category', 'category_display', 'created_at', 'updated_at', 'cover',
            'tags'
            ]

    def get_category_display(self, obj):
        return obj.category.title

    def get_cover(self, obj):
        if obj.cover:
            return obj.cover.url
        return '/'


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'