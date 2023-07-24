from django.contrib import admin

from .models import Profile
from .models import VehiculoModel

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificacion')


admin.site.register(VehiculoModel, VehiculoAdmin)
admin.site.register(Profile)
