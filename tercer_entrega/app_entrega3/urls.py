from django.urls import path
from app_entrega3.views import primer_vista,primer_template

urlpatterns = [
    path("",primer_vista),
    path("temp/",primer_template),
]
