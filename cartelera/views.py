from django.shortcuts import render
from cartelera.models import Pelicula

# Create your views here.
def mostrar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request,"mostrar_peliculas.html",{'peliculas':peliculas})