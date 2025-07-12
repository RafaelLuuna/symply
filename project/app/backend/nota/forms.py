from django import forms
from . import models

class NotaForm(forms.ModelForm):
    class Meta:
        model = models.Nota
        fields = [
            'titulo',
            'conteudo',
            'tipo',
            'data_acontecimento',
        ]