from django.db import models

class VehiculoModel(models.Model):
    MARCAS_OPTS = (
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    )

    CATEGORIAS_OPTS = (
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    )

    marca = models.CharField(max_length = 20, choices = MARCAS_OPTS, default = 'Ford')
    modelo = models.CharField(max_length = 100)
    serial_carroceria = models.CharField(max_length = 50)
    serial_motor = models.CharField(max_length = 50)
    categoria = models.CharField(max_length = 20, choices = CATEGORIAS_OPTS, default = 'Particular')
    precio = models.FloatField()
    fecha_creacion = models.DateTimeField(auto_now_add = True)
    fecha_modificacion = models.DateTimeField(auto_now = True)
    imagen = models.ImageField(upload_to='vehiculos', blank=True, null=True)

    class Meta:
        permissions = (
            ("visualizar_catalogo", "Permite ver el listado de vehiculos"),
            )

    def __str__(self):
        return self.marca