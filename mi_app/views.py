from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from mi_app.models import Curso, Estudiante, Profesor
from mi_app.forms import CursoBusquedaFormulario,CursoFormulario, EstudianteBusquedaFormulario, ProfesorBusquedaFormulario, ProfesorFormulario, EstudianteFormulario


def formulario_curso(request):

    if request.method == "POST":

        mi_formulario = CursoFormulario(request.POST)

        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            curso = Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()

            return render(request, "mi_app/formulario.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = CursoFormulario()

    return render(request, "mi_app/formulario.html", {"mi_formulario":mi_formulario})


def busqueda_curso(request):

    busqueda_curso = CursoBusquedaFormulario()

    if request.GET:     
        cursos = Curso.objects.filter(nombre=busqueda_curso["criterio"]).all()
        return render(request, "mi_app/busqueda.html", {"busqueda_curso": busqueda_curso, "cursos": cursos})


    return render(request, "mi_app/busqueda.html", {"busqueda_formulario": busqueda_curso})

def formulario_estudiante(request):

    if request.method == "POST":

        mi_formulario = EstudianteFormulario(request.POST)


        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            estudiantes = Estudiante(nombre=datos["nombre"], apellido=datos["apellido"], email=datos['email'])
            estudiantes.save()

            return render(request, "mi_app/form_estudiante.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = EstudianteFormulario()

    return render(request, "mi_app/form_estudiante.html", {"mi_formulario":mi_formulario})



def busqueda_estudiante(request):

    busqueda_estudiante = EstudianteBusquedaFormulario()


    if request.GET:     
        estudiantes = Estudiante.objects.filter(nombre=busqueda_estudiante["criterio"]).all()
        return render(request, "mi_app/search_estudiante.html", {"busqueda_estudiante": busqueda_estudiante, 'estudiantes': estudiantes})


    return render(request, "mi_app/search_estudiante.html", {"busqueda_estudiante": busqueda_estudiante})

def formulario_profesor(request):

    if request.method == "POST":

        mi_formulario = ProfesorFormulario(request.POST)


        if  mi_formulario.is_valid:
            datos = mi_formulario.cleaned_data 
            profesores = Profesor(nombre=datos["nombre"], apellido=datos["apellido"], email=datos['email'], profesion=datos['profesion'])
            profesores.save()

            return render(request, "mi_app/form_profesor.html", {"mensaje":"agregado con exito!"})

    else:

        mi_formulario = ProfesorFormulario()

    return render(request, "mi_app/form_profesor.html", {"mi_formulario":mi_formulario})



def busqueda_profesor(request):

    busqueda_profesor = ProfesorBusquedaFormulario()


    if request.GET:     
        profesores = Profesor.objects.filter(nombre=busqueda_profesor["criterio"]).all()
        return render(request, "mi_app/search_profesor.html", {"busqueda_profesor": busqueda_profesor, 'profesores': profesores})


    return render(request, "mi_app/search_profesor.html", {"busqueda_profesor": busqueda_profesor})

