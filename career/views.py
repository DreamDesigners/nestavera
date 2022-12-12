from rest_framework import generics
from career.models import (
  Job, JobSerializer, JobCategory,
  JobCategorySerializer, JobLocation, JobLocationSerializer,
  JobApplication, JobApplicationSerializer
  )
from url_filter.integrations.drf import DjangoFilterBackend


class JobsListView(generics.ListAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer
  filter_backends = (DjangoFilterBackend,)


class JobCategoryListView(generics.ListAPIView):
  queryset = JobCategory.objects.all()
  serializer_class = JobCategorySerializer
  filter_backends = (DjangoFilterBackend,)


class JobLocationListView(generics.ListAPIView):
  queryset = JobLocation.objects.all()
  serializer_class = JobLocationSerializer
  filter_backends = (DjangoFilterBackend,)


class JobApplicationCreateView(generics.CreateAPIView):
  queryset = JobApplication.objects.all()
  serializer_class = JobApplicationSerializer
  filter_backends = (DjangoFilterBackend,)