from django.db import models
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail


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


@receiver(post_save, sender=Contact)
def send_email_to_admin(sender, instance, created, **kwargs):
    if created:
        subject = "New Contact"
        message = f"Hello Admin, \n\nYou have a new contact from {instance.first_name} {instance.last_name} \n\nEmail: {instance.email} \n\nMessage: {instance.message} \n\nThank You"
        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        ['contact@nestavera.com', 'rahulbbhs1999@gmail.com', 'service@ddsio.com'],
        fail_silently=False,
        )


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'