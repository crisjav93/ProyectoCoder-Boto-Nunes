from django.urls import path
from .views import *

urlpatterns = [
    
    path('inicio/',inicio,name='inicio'),
    path('cursos/',curso,name="cursos"),
    path('profesores/',profesores,name="profesores"),
    path('perro/',perro,name="perro"),
    path('estudiantes/',estudiantes, name = 'estudiantes'),
    path('profeFormulario/',profeFormulario,name = 'profeFormulario'),
    path('cursoFormulario/',cursoFormulario,name="cursoFormulario"),
    path('estudianteFormulario/',estudiantesFormulario,name='estudianteFormulario'),
    path('perroFormulario/',perroFormulario, name ='perroFormulario'),
 
 
]