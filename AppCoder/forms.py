from django import forms

class CursoForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    comision= forms.IntegerField()

class ProfeForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)

class EstudianteForm(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()

class PerroForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    gustos = forms.CharField(max_length=50)