from django.urls import path

from .views import indexview, addvehiculo, login_view, logout_view, listvehiculo, registro_view, editvehiculo, deletevehiculo, myprofile, editprofile

handler403 = 'vehiculo.views.error_403_view'

urlpatterns = [
    path('', indexview, name = 'index'),
    path('add/', addvehiculo, name = 'addvehiculo'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('list/', listvehiculo, name = 'listvehiculo'),
    path('edit/<int:vehiculo_id>/', editvehiculo, name='editvehiculo'),
    path('delete/<int:vehiculo_id>/', deletevehiculo, name='deletevehiculo'),
    path('profile/', myprofile, name='profile'),
    path('profile/edit/', editprofile, name='editprofile'),
]
