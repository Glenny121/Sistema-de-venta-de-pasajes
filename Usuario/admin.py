from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    model = Usuario
    list_display = ('email','nombre','dni','is_active','is_staff')
    search_fields = ('email','nombre','dni','is_active','apellido','celular')
    fields = ['nombre','apellido','dni','celular','email','is_active','is_staff','is_superuser','fecha_creacion','fecha_actualizacion']
    readonly_fields = ('fecha_creacion','fecha_actualizacion')
    icon_name ='people'

admin.site.register(Usuario, UsuarioAdmin)
admin.site.unregister(Group)