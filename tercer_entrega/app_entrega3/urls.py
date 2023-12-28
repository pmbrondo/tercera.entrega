from django.urls import path
from app_entrega3.views import pag_inicio,tema,artista,disco,miformulario,vista_compositor

urlpatterns = [

    path("",pag_inicio,name='inicio.html'),
    path("tema/",tema,name='tema.html'),
    path("artista/",artista,name='artista.html'),
    path("disco/",disco,name='disco.html'),
    path("formulario",miformulario,name="miformulario.html"),
    path("respuesta",vista_compositor,name="respuesta.html"),
]
