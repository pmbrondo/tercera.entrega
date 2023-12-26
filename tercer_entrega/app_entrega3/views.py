from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def pag_inicio(request):
    return render(request,"inicio.html")



def tema(request):
    return render(request,'tema.html')


def artista(request):
    return render(request,'artista.html')

def disco(request):
    return render (request,'disco.html')