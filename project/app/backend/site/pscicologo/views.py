from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect


### VIEWS COMUNS ###
@require_http_methods(['GET'])
@login_required
def minhas_notas(request):
    notas = models.Nota.objects.all()
    context = {
        'notas': notas,
    }
    return render(request, 'site/nota/minhas_notas.html', context)

@require_http_methods(['GET','POST'])
@login_required
def home(request):
    return render(request, 'site/home.html')





