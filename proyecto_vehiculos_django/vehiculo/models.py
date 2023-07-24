from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='profile_avatars/avatar.jpg', # default avatar
        upload_to='profile_avatars' # dir to store the image
    )

    biography = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)

        # resize the image
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            # overwrite the larger image
            img.save(self.avatar.path)