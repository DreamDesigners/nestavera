from django.contrib import admin
from .models import Job, JobLocation, JobCategory, JobApplication

admin.site.register(JobLocation)
admin.site.register(JobCategory)
admin.site.register(Job)
admin.site.register(JobApplication)