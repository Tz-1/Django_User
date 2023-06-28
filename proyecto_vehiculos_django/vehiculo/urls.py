from django.contrib import admin
from django.urls import path

from .views import indexview, addvehiculo, login_view, logout_view, listvehiculo, registro_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexview, name = 'index'),
    path('vehiculo/add', addvehiculo, name = 'addvehiculo'),
    path('registro/', registro_view, name='registro'),
    path('login', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('vehiculo/list', listvehiculo, name = 'listvehiculo')
]
