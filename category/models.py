from django.db import models
from rest_framework import serializers


class Category(models.Model):
  parent        = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
  title         = models.CharField(max_length=255, unique=True)
  slug          = models.SlugField(max_length=500, unique=True)

  is_active     = models.BooleanField(default=True)
  created_at    = models.DateTimeField(auto_now_add=True)
  updated_at    = models.DateTimeField(auto_now=True)


  def __str__(self):
        return self.title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
