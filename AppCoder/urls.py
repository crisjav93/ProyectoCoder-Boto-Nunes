from django.urls import path
from .views import *

urlpatterns = [
    path('cursos/',curso,name="cursos"),
    path('profesores/',profesores,name="profesores"),
    path('perro/',perro,name="perro"),
    path('cursoFormulario/',cursoFormulario,name="cursoFormulario"),
    path('inicio/',inicio,name='inicio'),
    path('profeFormulario/',profeFormulario,name = 'profeFormulario'),
    path('estudiantes/',estudiantes, name = 'estudiantes'),
]