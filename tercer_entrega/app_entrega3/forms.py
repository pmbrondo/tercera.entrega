
from django import forms


class Buscar_datos(forms.Form):
    buscodisco=forms.CharField(max_length=20)