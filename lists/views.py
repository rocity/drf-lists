from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .models import List, Item


class ListViewSet(ViewSet):
    queryset = List.objects.all()
