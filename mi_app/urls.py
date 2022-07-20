from django.contrib import admin
from django.urls import path
from mi_app.views import formulario_cliente, formulario_supermercado, formulario_vendedor, busqueda_cliente, busqueda_super, busqueda_vendedor, base
from . import views

urlpatterns = [
    path('inicio', base, name='Inicio'),
    path('sucursal/', views.formulario_supermercado, name ='Sucursal'),
    path('vendedor/', views.formulario_vendedor, name='Vendedor'),
    path('cliente/', views.formulario_cliente, name= 'Servicio al Cliente'),
    path('buscarcliente/', views.busqueda_cliente, name = 'Buscar cliente'),
    path('buscarvendedor/', views.busqueda_vendedor, name= 'Buscar vendedor'),
    path('buscarsucursal/', views.busqueda_super, name='Buscar sucursal'),

]