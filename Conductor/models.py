from django.db import models
from django.utils.html import format_html

class Conductor(models.Model):
# Create your models here.
    nombre = models.CharField(
        max_length=20,
        null=True,
        verbose_name="Nombre"
    )
    apellidos= models.CharField(
        max_length=20,
        null=True,
        verbose_name="Apellidos"
    )
    dni = models.IntegerField(
        null=True,
        verbose_name="DNI"
    )
    celular = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name='Celular'
    )
    foto_conductor = models.ImageField(
        null =True,
        blank = True,
        upload_to = "Conductor/picture",
        default = None,
        verbose_name = "Imagen"
    )
    estado = models.BooleanField(
        default=True,
        verbose_name='Estado'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Fecha Creacion")

    fecha_actualizacion = models.DateTimeField(
        auto_now = True,
         verbose_name = "Fecha Actualizacion")

    def image_tag(self):
        try:
            return format_html('<img src={} width="100", heigth="100" />', self.foto_conductor.url)
        except:
            pass
    image_tag.allow_tags = True  

    def __str__(self):
        return "{0}".format(self.nombre + ' ' + self.apellidos )
    
    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"