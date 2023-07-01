from django.db import models
from rest_framework import serializers


class Tag(models.Model):
  name        = models.CharField(max_length=255, unique=True)
  is_active     = models.BooleanField(default=True)

  def __str__(self):
    return self.name


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class Category(models.Model):
  parent        = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
  title         = models.CharField(max_length=255, unique=True)
  slug          = models.SlugField(max_length=500, unique=True)
  file          = models.FileField(upload_to='category/', blank=True, null=True)

  is_active     = models.BooleanField(default=True)
  created_at    = models.DateTimeField(auto_now_add=True)
  updated_at    = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
