
from . import forms
from . import models

from django.http import HttpResponseRedirect 
from django.views.decorators.http import require_http_methods

from django.contrib.auth.decorators import login_required

from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

### VIEWS DE SITE ###
@require_http_methods(['GET'])
@login_required
def info(request, id):
    nota = get_object_or_404(models.Nota, pk=id)
    context = {
        'nota': nota,
    }
    return render(request, 'site/nota/info.html', context)


@require_http_methods(['GET'])
@login_required
def minhas_notas(request):
    notas = models.Nota.objects.all().order_by('-data_acontecimento')
    context = {
        'notas': notas,
    }
    return render(request, 'site/nota/minhas_notas.html', context)


### VIEWS DE API ###
@require_http_methods(['GET','POST'])
@login_required
def cadastro(request, id=None):

    ### LIDA COM REQUISIÇÕES VINDAS DE FORMULÁRIOS ###
    if request.method == 'POST':

        if(id is not None):
            nota = get_object_or_404(models.Nota, pk=id)
            form = forms.NotaForm(request.POST, instance=nota)
        else:
            form = forms.NotaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'nota registrada com sucesso!')
            response = HttpResponseRedirect(reverse('paciente:minhas_notas'))
        else:
            form.add_error(None, 'Dados inválidos.')
            context = {
                'form': form,
            }
            response = render(request, 'site/nota/cadastro.html', context)
    
    ### LIDA COM REQUISIÇÕES VINDAS DE UM BROWSER ###
    elif request.method == 'GET':

        if(id is None):
            form = forms.NotaForm()
        else:
            nota = get_object_or_404(models.Nota, pk=id)
            form = forms.NotaForm(instance=nota)

        
        context = {
            'form': form,
            'id': id,
        }
        
        response = render(request, 'site/nota/cadastro.html', context)

    ### NÃO LIDA COM NADA, SE CHEGAR AQUI DESCONFIE ###
    else:
        response = HttpResponseForbidden('Não era pra você chegar aqui nem por milagre...')


    return response


@require_http_methods(['GET'])
@login_required
def delete(request, id):
    nota = get_object_or_404(models.Nota, pk=id)
    messages.success(request, 'nota deletada com sucesso!')
    nota.delete()
    return HttpResponseRedirect(reverse('paciente:minhas_notas'))