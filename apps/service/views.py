from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import ServiceSerializer
from .models import Services
from rest_framework.permissions import AllowAny


class ServiceView(generics.ListAPIView):
    permission_classes = AllowAny,
    serializer_class = ServiceSerializer
    queryset = Services.objects.all()
