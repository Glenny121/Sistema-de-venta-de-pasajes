from django.db import models
from Conductor.models import Conductor

class Bus(models.Model):
    placa = models.CharField(
        max_length = 7,
        null=True,
        blank=False,
        verbose_name="Bus"
    )
    capacidad = models.IntegerField(
        null=True,
        verbose_name='Capacidad'
    )
    conductor = models.ForeignKey(
        Conductor,
        null=True,
        blank=True,
        verbose_name='Conductor',
        on_delete=models.CASCADE
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
    
    def __str__(self):
        return "{0}".format(self.placa )
    
    class Meta:
        verbose_name = 'Bus'
        verbose_name_plural = 'Buses'
