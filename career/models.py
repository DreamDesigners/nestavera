from django.db import models
from rest_framework import serializers
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail


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


class JobLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = '__all__'


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'


class JobApplication(models.Model):
  job    = models.ForeignKey(Job, on_delete=models.CASCADE)
  name   = models.CharField(max_length=255)
  email  = models.EmailField()
  phone  = models.CharField(max_length=12)
  resume = models.FileField(upload_to='resumes/')

  def __str__(self):
    return str(self.name)


# send email to admin when a new job application is submitted
@receiver(post_save, sender=JobApplication)
def send_job_application_email(sender, instance, created, **kwargs):
    if created:
        subject = "New Job Application"
        message = "A new job application has been submitted."
        # include details of the job application in the email
        message += "\n\nJob: " + instance.job.title
        message += "\nName: " + instance.name
        message += "\nEmail: " + instance.email
        message += "\nPhone: " + instance.phone

        recipient_list = ['contact@nestavera.com']
        # recipient_list = ['harsh@ddsio.com']
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)





class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'