from rest_framework import generics
from career.models import Job, JobSerializer, JobCategory, JobCategorySerializer, JobLocation, JobLocationSerializer
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
  queryset = Job.objects.all()
  serializer_class = JobLocationSerializer
  filter_backends = (DjangoFilterBackend,)