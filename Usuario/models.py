from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from django.utils.html import format_html


class UsarioManager(BaseUserManager):

    def create_user(self,email,nombre,dni,password=None):

        '''Crear nuevo Usuario'''

        if not email:
            raise ValueError('Usuario debe tener un Email')

        email = self.normalize_email(email)
        user = self.model(email=email,nombre=nombre,dni=dni)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,nombre,dni,password):
        user = self.create_user(email,nombre,dni,password)
        user.is_superuser  = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser,PermissionsMixin):

    '''Modelo BD para usuarios en el sistema'''

    email = models.EmailField(max_length=255,unique=True, verbose_name="Email", null=False, blank=False)
    nombre = models.CharField(max_length=255, null=False, blank=False, verbose_name="Nombre")
    apellido =models.CharField(max_length=255, null=True, blank=True,verbose_name="Apellido")
    is_active = models.BooleanField(default=True, verbose_name="Esta activo") #Estado del usuario (estado logico)
    is_staff = models.BooleanField(default=False, verbose_name="Es administrador")#(Estado de administrador-tipo)
    dni =models.IntegerField(unique=True, null=False, blank=False, verbose_name="DNI")
    celular = models.IntegerField(null=True, blank= True, verbose_name="Celular")
    is_superuser = models.BooleanField(default=False, verbose_name="Permiso administrador")
    fecha_creacion = models.DateTimeField(auto_now_add = True, verbose_name = "Fecha Creacion")
    fecha_actualizacion = models.DateTimeField(auto_now = True, verbose_name = "Fecha Actualizacion")

    
    '''DJANGO customización del modelo'''

    objects = UsarioManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre','dni']

    # def get_full_name(self):
    #     ''' Obtener nombre completo del usuario'''
    #     return self.name_completed

    def get_short_name(self):
        ''' Obtener nombre corto del usuario '''
        return self.nombre
        
    def _str_(self):
        '''retornar cadena'''
        return self.email

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
