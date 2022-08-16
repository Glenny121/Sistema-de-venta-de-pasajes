from django.contrib import admin
from .models import Boleta
# Register your models here.
class BoletaAdmin(admin.ModelAdmin):
    def precioTotal(self,obj):
        res =  float(obj.precio) * float(obj.asientos)
        return 'S/' + str(res)
    precioTotal.admin_order_field = 'Precio Total'
    precioTotal.short_description= 'Precio Total'

    model = Boleta
    list_display = ('usuario','ruta','asientos','horaSalida','precio','precioTotal','estado')
    search_fields = ('usuario','ruta','horaSalida')
    fields = ['usuario','ruta','asientos','horaSalida','precio','estado','fecha_creacion','fecha_actualizacion']
    readonly_fields = ('fecha_creacion','fecha_actualizacion')
    icon_name = 'assignment'

admin.site.register(Boleta,BoletaAdmin)