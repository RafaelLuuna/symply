from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseForbidden

from authentication import api

from . import forms

@require_http_methods(['GET','POST'])
def login(request):
    logout(request)

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        response = api.LoginApi(request, form)

        
    elif request.method == 'GET':
        form = forms.LoginForm()
        context = {
            'form': form,
        }
        
        response = render(request, 'auth/login.html', context)

    else:
        response = HttpResponseForbidden('Não era pra você chegar aqui nem por milagre, pilantrinha...')


    return response


@require_http_methods(['GET','POST'])
def cadastro(request):
    logout(request)

    if request.method == 'POST':
        form = forms.CadastroForm(request.POST)
        response = api.CadastroApi(request, form)

    elif request.method == 'GET':
        form = forms.CadastroForm()
        context = {
            'form': form,
        }
        
        response = render(request, 'auth/cadastro.html', context)

    else:
        response = HttpResponseForbidden('Não era pra você chegar aqui nem por milagre, pilantrinha...')
    

    return response


def logout(request):
    return api.LogoutApi(request)