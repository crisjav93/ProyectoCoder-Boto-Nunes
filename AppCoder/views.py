from django.http import HttpResponse
from django.shortcuts import render
from .models import * 
from AppCoder.forms import *

def inicio(request):
    return render(request, 'Appcoder/inicio.html')
def curso(request):
    return render(request,"AppCoder/curso.html")
def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")
def profesores(request):
    return render(request,"AppCoder/profesores.html")
def perro(request):
    return render(request,"AppCoder/perro.html")


def curso(self):
    curso = Curso(nombre='Django',comision=93123)
    curso.save()
    texto=f'Curso creado: {curso.nombre} {curso.comision}'
    return HttpResponse(texto)


def cursoFormulario(request):
    form= CursoForm(request.POST)
    if form.is_valid():
        info = form.cleaned_data
        nombre = info['nombre']
        comision = info['comision']
        curso=Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, 'Appcoder/inicio.html')
    else:
        form = CursoForm()
    return render(request, 'AppCoder/cursoFormulario.html',{'formulario':form})


def profeFormulario(request):
    form = ProfeForm(request.POST)
    if form.is_valid():
        info = form.cleaned_data
        nombre = info['nombre']
        apellido = info['apellido']
        email = info['email']
        profesion= info['profesion']
        profesor=Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
        profesor.save()
        return render(request, 'Appcoder/inicio.html')
    else:
        form = ProfeForm()
    return render(request, 'Appcoder/profeFormulario.html',{'formulario':form})
