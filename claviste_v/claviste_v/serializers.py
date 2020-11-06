from rest_framework import serializers
from mantenedor.models import regitro_cliente


class registroClienteSerializers(serializers.ModelSerializer):

    class Meta:
        model=regitro_cliente
        fields = ['nombre','apellidoP','apellidoM','email','telefono']