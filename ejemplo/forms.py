from django import forms
from ejemplo.models import Familiar, Mascota, Vehiculo

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100, widget = forms.TextInput(attrs= {'placeholder': 'Busque algo..'}))

class BuscarMascota(forms.Form):
    apodo = forms.CharField(max_length=100, widget = forms.TextInput(attrs= {'placeholder': 'Busque algo..'}))

class BuscarVehiculo(forms.Form):
    marca = forms.CharField(max_length=100, widget = forms.TextInput(attrs= {'placeholder': 'Busque algo..'}))

class FamiliarForm(forms.ModelForm):
  class Meta:
    model = Familiar
    fields = ['nombre', 'direccion', 'numero_pasaporte']

class MascotaForm(forms.ModelForm):
  class Meta:
    model = Mascota
    fields = ['apodo', 'raza', 'edad']

class VehiculoForm(forms.ModelForm):
  class Meta:
    model = Vehiculo
    fields = ['marca', 'modelo', 'patente']