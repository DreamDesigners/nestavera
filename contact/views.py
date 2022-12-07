from rest_framework import generics
from contact.models import Contact, ContactSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class ContactsCreateView(generics.CreateAPIView):
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
  filter_backends = (DjangoFilterBackend,)