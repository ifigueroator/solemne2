from django.contrib import admin

from mantenedor.models import regitro_cliente,nuevos_plan

class nuevoCliente(admin.ModelAdmin):
    list_display=("nombre","apellidoP","apellidoM","email","telefono")

class registro(admin.ModelAdmin):
    list_display=("nombre_plan","precio_plan","fecha_inicio","fecha_termino")

admin.site.register(regitro_cliente,nuevoCliente)
admin.site.register(nuevos_plan,registro)
