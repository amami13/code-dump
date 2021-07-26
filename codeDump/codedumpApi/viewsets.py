from rest_framework.viewsets import ModelViewSet
from . serializers import *


class FileViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = FileSerializer
    queryset = File.objects.all()


class FileVersionViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = FileVersionSerializer
    queryset = FileVersion.objects.all()
