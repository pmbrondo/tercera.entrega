from django.urls import path
from app_entrega3.views import primer_vista

urlpatterns = [
    path("",primer_vista),
]
