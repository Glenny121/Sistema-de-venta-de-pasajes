from django.db import models
from Usuario.models import Usuario
from Ruta.models import Ruta

class Boleta(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        null=True,
        blank=True,
        verbose_name='Usuario',
        on_delete = models.DO_NOTHING
    )
    ruta = models.ForeignKey(
        Ruta,
        null=True,
        blank=True,
        verbose_name='Ruta',
        on_delete = models.DO_NOTHING
    )
    asientos = models.IntegerField(
        null=True,
        verbose_name='Asientos'
    )
    precio = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=False,
        verbose_name='Precio Unidad'
    )
    horaSalida = models.DateTimeField(
        verbose_name='Fecha y Hora de Salida'
    )
    estado = models.BooleanField(
        default=True,
        verbose_name='Estado'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Fecha Creacion"
    )
    fecha_actualizacion = models.DateTimeField(
        auto_now = True,
        verbose_name = "Fecha Actualizacion"
    )
    class Meta:
        verbose_name = 'Boleta'
        verbose_name_plural = 'Boletas'