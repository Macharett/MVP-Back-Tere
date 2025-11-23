from rest_framework import viewsets
from django.db.models import Q
from django.utils import timezone
from .models import Parque
from .serializers import ParqueSerializer

class ParqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Parque.objects.all()
    serializer_class = ParqueSerializer