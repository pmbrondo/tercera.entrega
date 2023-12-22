from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def primer_vista(request):
    return HttpResponse("Hello")


def primer_template(request):

    variablemias={
        "nombre":"Matias",
        "edad":34,
    }
    return  render(request, "primera.html",variablemias)