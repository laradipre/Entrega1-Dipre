from django.contrib import admin
from django.urls import path
from mi_app.views import formulario_curso, busqueda_curso, formulario_estudiante, busqueda_estudiante,formulario_profesor, busqueda_profesor


urlpatterns = [
    path('form_curso/', formulario_curso),
    path('form_estudiante', formulario_estudiante),
    path('form_profesor', formulario_profesor),
    path('search_curso', busqueda_curso),
    path('search_estudiante', busqueda_estudiante),
    path('search_profesor', busqueda_profesor),
]