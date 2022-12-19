"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ejemplo.views import index, saludar_a, sumar, buscar, monstrar_familiares, BuscarFamiliar, AltaFamiliar, ActualizarFamiliar, BorrarFamiliar, mostrar_mascotas, mostrar_vehiculos, BuscarMascota, BuscarVehiculo, ActualizarMascota, ActualizarVehiculo, BorrarMascota, BorrarVehiculo, AltaMascota, AltaVehiculo, FamiliarDetalle, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('saludar-a/<nombre>', saludar_a),
    path('sumar/<int:a>/<int:b>/', sumar),
    path('buscar/', buscar),
    path('mi-familia/', monstrar_familiares),
    path('mi-familia/buscar', BuscarFamiliar.as_view(), name= 'mi-familia/buscar'),
    path('mi-familia/alta', AltaFamiliar.as_view(), name= 'mi-familia/alta'),
    path('mi-familia/actualizar/<int:pk>', ActualizarFamiliar.as_view()),
    path('mi-familia/borrar/<int:pk>', BorrarFamiliar.as_view()),
    path('mi-mascota/', mostrar_mascotas),
    path('mi-mascota/buscar', BuscarMascota.as_view()),
    path('mi-mascota/alta', AltaMascota.as_view()),
    path('mi-mascota/actualizar/<int:pk>', ActualizarMascota.as_view()),
    path('mi-mascota/borrar/<int:pk>', BorrarMascota.as_view()),
    path('mi-vehiculo/', mostrar_vehiculos),
    path('mi-vehiculo/buscar', BuscarVehiculo.as_view()),
    path('mi-vehiculo/alta', AltaVehiculo.as_view()),
    path('mi-vehiculo/actualizar/<int:pk>', ActualizarVehiculo.as_view()),
    path('mi-vehiculo/borrar/<int:pk>', BorrarVehiculo.as_view()),
    path('panel-familia/<int:pk>/detalle', FamiliarDetalle.as_view()),
    path('panel-familia/', FamiliarList.as_view()),
    path('panel-familia/crear', FamiliarCrear.as_view()),
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view()),
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view()),
    path('succes_updated_message', TemplateView.as_view(template_name ='ejemplo/succes_updated_message.html')),
    ]
