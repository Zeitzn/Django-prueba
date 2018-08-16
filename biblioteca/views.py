from django.shortcuts import render
from django.http import HttpResponse
from biblioteca.models import Libro
# Create your views here.

def formulario_buscar(request):
    return render(request,'formulario_buscar.html')

def buscar(request):
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Por favor introduce un término de búsqueda')
        elif len(q)>20:
            errors.append('Por favor introduce un término de búsqueda menor a 30 caractéres')
        else:
            libros=Libro.objects.filter(titulo__icontains=q)
            return render(request,'resultados.html',{'libros':libros,'query':q})
    return render(request,'formulario_buscar.html',{'errors':errors})
