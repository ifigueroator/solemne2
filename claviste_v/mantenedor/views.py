from django.shortcuts import render

from rest_framework import viewsets
from mantenedor.models import regitro_cliente

from claviste_v.serializers import registroClienteSerializers

class registroClienteViewset(viewsets.ModelViewSet):
    queryset = regitro_cliente.objects.all()
    serializer_class=registroClienteSerializers
