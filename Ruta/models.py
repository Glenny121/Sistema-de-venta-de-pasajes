from django.db import models
from Bus.models import Bus
# Create your models here.
class Ruta(models.Model):
    RUTAS_CHOICES=[
        ("AR",'Arequipa'),
        ("CZ",'Cuzco'),
        ("AY",'Ayacucho'),
        ("IC",'Ica'),
        ("PU","Puno"),
        ("HU","Huanuco"),
    ]
    origen = models.CharField(
        max_length=2,
        choices=RUTAS_CHOICES,
        verbose_name='Origen'
    )
    destino = models.CharField(
        max_length=2,
        choices=RUTAS_CHOICES,
        verbose_name='Destino'
    )
    precio = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=False,
        verbose_name='Precio'
    )
    estado = models.BooleanField(
        default=True,
        verbose_name='Estado'
    )
    bus = models.ForeignKey(
        Bus,
        blank=True, 
        verbose_name='Bus',
        on_delete=models.CASCADE,

    )
    fecha_creacion = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Fecha Creacion")

    fecha_actualizacion = models.DateTimeField(
        auto_now = True,
        verbose_name = "Fecha Actualizacion")
    #Reconfigurando el metodo guardar 
    def save(self,*args,**kawargs):
        print(self.origen, self.destino)
        if self.origen != self.destino:
            super().save(*args,**kawargs)
    
    def __str__(self):
        return "{0}".format(self.origen + ' - ' + self.destino )
    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'