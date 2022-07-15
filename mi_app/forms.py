from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField(required=False)
    camada = forms.IntegerField()

class CursoBusquedaFormulario(forms.Form):
    criterio = forms.CharField() 

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    email= forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(required=False)
    apellido = forms.CharField(required=False)
    email=forms.EmailField()
    profesion = forms.CharField(required=False)

class EstudianteBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

class ProfesorBusquedaFormulario(forms.Form):
    criterio = forms.CharField()

