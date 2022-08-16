from django.contrib import admin
from .models import Bus
# Register your models here.
class BusAdmin(admin.ModelAdmin):
    model = Bus
    list_display = ('placa','conductor','capacidad','estado')
    search_fields = ('placa','conductor','capacidad')
    fields = ['placa','conductor','capacidad','estado','fecha_creacion','fecha_actualizacion']
    readonly_fields = ('fecha_creacion','fecha_actualizacion')
    icon_name = 'directions_bus'
    
admin.site.register(Bus,BusAdmin)