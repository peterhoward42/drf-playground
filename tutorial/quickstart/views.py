from django.contrib.auth.models import User, Group

from rest_framework import viewsets

# Note this import is from rest_framework - despite there being
# one of the same name in django_filters. Using the wrong one generates
# OrderingFilter' object has no attribute 'filter_queryset'
from rest_framework.filters import OrderingFilter

from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, InvoiceSerializer
from tutorial.quickstart.models import Invoice


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class InvoiceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows invoices to be viewed.
    """
    queryset = Invoice.objects.all().order_by('big')
    serializer_class = InvoiceSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ['big', 'amount']

