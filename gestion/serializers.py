from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Vehiculo, Marca


class VehiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class MarcaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'
