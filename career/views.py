from rest_framework import generics
from career.models import Job, JobSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class JobsListView(generics.ListAPIView):
  queryset = Job.objects.all()
  serializer_class = JobSerializer
  filter_backends = (DjangoFilterBackend,)