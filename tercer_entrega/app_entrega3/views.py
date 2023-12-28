from django.shortcuts import render
from django.http import HttpResponse
from app_entrega3.models import *


# Create your views here.
def vista_compositor(request):
    compositor=Compositor.objects.all()
    return render(request,"respuesta.html",{"compositor":compositor})

def tema(request):
    tema=Temas.objects.all()
    return render(request,'tema.html',{"tema":tema})


def disco(request):
    disco=Disco.objects.all()
    return render (request,'disco.html',{"disco":disco})


def pag_inicio(request):
    return render(request,"inicio.html")






def artista(request):
    return render(request,'artista.html')



def miformulario(request):
    if request.method=="POST":
        #Compositor
        a=request.POST.get("nombre")
        b=request.POST.get("disco")
        #Temas
        c=request.POST.get("nombre_tema")
        d=request.POST.get("duracion")
        #Disco
        e=request.POST.get("nombre_disco")
        f=request.POST.get("artista_disco")
        g=request.POST.get("duracion_disco")
        #Compositor
        compositorfor=Compositor(nombre=a,disco=b)
        compositorfor.save()
        #Temas
        temafor=Temas(nombre_tema=c,duracion=d)
        temafor.save()
        #Disco
        discofor=Disco(nombre_disco=e,artista_disco=f,duracion_disco=g)
        discofor.save()

        return render (request, "inicio.html")



        print(a,b,c,d,e,f,g)
    return render(request,'miformulario.html')




        