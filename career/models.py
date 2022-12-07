from django.db import models
from rest_framework import serializers


class JobLocation(models.Model):
  title  = models.CharField(max_length=500, unique=True)

  def __str__(self):
    return self.title


class JobCategory(models.Model):
  title  = models.CharField(max_length=500, unique=True)

  def __str__(self):
    return self.title


class Job(models.Model):
  location        = models.ForeignKey(JobLocation, on_delete=models.CASCADE)
  category        = models.ForeignKey(JobCategory, on_delete=models.CASCADE)

  title           = models.CharField(max_length=500)
  slug            = models.SlugField(max_length=500, unique=True)
  body            = models.TextField()

  is_featured   = models.BooleanField(default=False)
  is_active     = models.BooleanField(default=True)
  created_at    = models.DateTimeField(auto_now_add=True)
  updated_at    = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

class Meta:
    ordering = ['-updated_at']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'