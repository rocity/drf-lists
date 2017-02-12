from rest_framework import viewsets
from rest_framework.response import Response

from .models import List, Item
from .serializers import ListSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
