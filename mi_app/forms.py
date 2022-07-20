from django import forms

class SupermercadoFormulario(forms.Form):
    sucursal = forms.CharField(required=False)
    empleados = forms.IntegerField()

class SuperBusquedaFormulario(forms.Form):
    criterio = forms.CharField() 

class VendedorFormulario(forms.Form):
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    numero_de_caja= forms.IntegerField()

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    email=forms.EmailField()

class VendedorBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

class ClienteBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

