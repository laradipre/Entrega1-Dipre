from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Supermercado, Vendedor, Cliente
from mi_app.forms import SuperBusquedaFormulario, SupermercadoFormulario, VendedorBusquedaFormulario, VendedorFormulario, ClienteBusquedaFormulario, ClienteFormulario

def base(request):
    return render (request, 'entrega_1/base.html', {})

def formulario_supermercado(request):

    if request.method == "POST":

        mi_formulario = SupermercadoFormulario(request.POST)

        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            super = Supermercado(sucursal=datos["sucursal"], empleados=datos["cantidad de empleados"])
            super.save()

            return render(request, "entrega_1/sucursal.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = SupermercadoFormulario()

    return render(request, "entrega_1/sucursal.html", {"mi_formulario":mi_formulario})


def busqueda_super(request):

    busqueda_super = SuperBusquedaFormulario()

    if request.GET:     
        supers = Supermercado.objects.filter(sucursal=busqueda_super["criterio"]).all()
        return render(request, "entrega_1/busqueda.html", {"busqueda_super": busqueda_super, "supermercados": supers})


    return render(request, "entrega_1/busqueda.html", {"busqueda_formulario": busqueda_super})

def formulario_vendedor(request):

    if request.method == "POST":

        mi_formulario = VendedorFormulario(request.POST)


        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            vendedores = Vendedor(nombre=datos["nombre"], apellido=datos["apellido"], numero_de_caja=datos['numero de caja'])
            vendedores.save()

            return render(request, "entrega_1/vendedor.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = VendedorFormulario()

    return render(request, "entrega_1/vendedor.html", {"mi_formulario":mi_formulario})



def busqueda_vendedor(request):

    busqueda_vendedor = VendedorBusquedaFormulario()


    if request.GET:     
        vendedores = Vendedor.objects.filter(nombre=busqueda_vendedor["criterio"]).all()
        return render(request, "entrega_1/buscarvendedor.html", {"busqueda_vendedor": busqueda_vendedor, 'vendedores': vendedores})


    return render(request, "entrega_1/buscarvendedor.html", {"busqueda_estudiante": busqueda_vendedor})

def formulario_cliente(request):

    if request.method == "POST":

        mi_formulario = ClienteFormulario(request.POST)


        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            clientes = Cliente(nombre=datos["nombre"], apellido=datos["apellido"], email=datos['email'])
            clientes.save()

            return render(request, "entrega_1/cliente.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = ClienteFormulario()

    return render(request, "entrega_1/cliente.html", {"mi_formulario":mi_formulario})



def busqueda_cliente (request):

    busqueda_cliente = ClienteBusquedaFormulario()


    if request.GET:     
        clientes = Cliente.objects.filter(nombre=busqueda_cliente["criterio"]).all()
        return render(request, "entrega_1/buscarcliente.html", {"busqueda_cliente": busqueda_cliente, 'clientes': clientes})


    return render(request, "entrega_1/buscarcliente.html", {"busqueda_cliente": busqueda_cliente})

