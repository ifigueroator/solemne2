from django.db import models

class regitro_cliente(models.Model):
    nombre=models.CharField(max_length=30)
    apellidoP=models.CharField(max_length=30)
    apellidoM=models.CharField(max_length=30)
    email=models.EmailField()
    telefono=models.CharField(max_length=9)

    class nuevos_plan(models.Model):
        nombre_plan=models.CharField(max_length=30)
        precio_plan=models.IntegerField()
        fecha_inicio=models.DateField()
        fecha_termino=models.DateField()
    

    

