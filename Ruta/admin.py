from django.contrib import admin
from .models import Ruta
# Register your models here.
class RutaAdmin(admin.ModelAdmin):
    model = Ruta
    list_display = ('origen','destino','precio','estado')
    search_fields = ('origen','destino','precio','estado')
    fields= ['origen','destino','precio','estado','bus','fecha_creacion','fecha_actualizacion']
    readonly_fields = ('fecha_creacion','fecha_actualizacion') 
    icon_name = 'compare_arrows'

admin.site.register(Ruta,RutaAdmin)