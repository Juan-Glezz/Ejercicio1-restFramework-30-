from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,filters
from .permissions import VehiculoPermission
from .serializers import MarcaSerializer, VehiculoSerializer
from .models import Marca, Vehiculo


class VehiculoView(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [VehiculoPermission]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['marca','modelo','color']
    ordering_fields = ['fecha_fabricacion']


class MarcaView(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    permission_classes = [VehiculoPermission]
    filter_backends = [DjangoFilterBackend]


