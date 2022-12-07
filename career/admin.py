from django.contrib import admin
from .models import Job, JobLocation, JobCategory

admin.site.register(JobLocation)
admin.site.register(JobCategory)
admin.site.register(Job)