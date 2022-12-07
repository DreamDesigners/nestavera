from django.db import models
from rest_framework import serializers


class Contact(models.Model):
  first_name      = models.CharField(max_length=244)
  last_name       = models.CharField(max_length=244)
  email           = models.EmailField()
  message         = models.TextField()

  is_reviewd      = models.BooleanField(default=False)
  created_at      = models.DateTimeField(auto_now_add=True)
  updated_at      = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.first_name

class Meta:
    ordering = ['-updated_at']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'