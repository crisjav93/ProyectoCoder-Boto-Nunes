from django.http import HttpResponse
from django.shortcuts import render
from .models import * 
from AppCoder.forms import *

def inicio(request):
    return render(request, 'Appcoder/inicio.html')
def curso(request):
    return render(request,"AppCoder/cursos.html")
def estudiantes(request):
    return render(request,"AppCoder/estudiantes.html")
def profesores(request):
    return render(request,"AppCoder/profesores.html")
def perro(request):
    return render(request,"AppCoder/perro.html")

def cursoFormulario(request):
    if (request.method=='POST'):
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
    if (request.method=='POST'):
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

def estudiantesFormulario(request):
    if (request.method=='POST'):
        form= EstudianteForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            apellido = info['apellido']
            email = info['email']
            estudiante= Estudiante(nombre=nombre, apellido=apellido, email=email)
            estudiante.save()
            return render(request, 'Appcoder/inicio.html')
    else:
        form=EstudianteForm()
    return render(request,'Appcoder/estudianteFormulario.html',{'formulario':form})

def perroFormulario(request):
    if (request.method=='POST'):
        form= PerroForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info['nombre']
            gustos = info['gustos']
            perro= Perro(nombre=nombre, gustos=gustos)
            perro.save()
            return render(request, 'Appcoder/inicio.html')
    else:
        form=PerroForm()
    return render(request,'Appcoder/perroFormulario.html',{'formulario':form})
