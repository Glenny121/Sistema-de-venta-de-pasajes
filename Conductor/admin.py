from django.contrib import admin
from .models import Conductor

class ConductorAdmin(admin.ModelAdmin):
    model = Conductor
    ordering = ('-fecha_creacion',)
    list_display = ('nombre','apellidos','dni','celular','image_tag','estado')
    search_fields = ('nombre','apellidos','dni','celular')
    fields= ['nombre','apellidos','dni','celular','foto_conductor','image_tag','estado','fecha_creacion','fecha_actualizacion']
    readonly_fields = ('image_tag','fecha_creacion','fecha_actualizacion') 
    icon_name = 'account_circle'

admin.site.register(Conductor,ConductorAdmin)

# Register your models here.
