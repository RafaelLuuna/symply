from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect 
from django.views.decorators.http import require_POST

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

from authentication.models import CustomUser, ROLES
from . import forms

@require_POST
def LoginApi(request, form):
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
    User = authenticate(
        username=username,
        password=password
    )
    
    if User is not None:
        login(request, User)
        redirectUrl = ROLES[User.role]['default_page']
        return HttpResponseRedirect(redirectUrl)


    # Por padrão, caso a API não consiga encontrar o usuário, renderizará a view de login
    form.add_error(None, 'Usuário ou senha inválidos.')
    context = {
        'form': form,
    }
    return render(request, 'auth/login.html', context)
    

@require_POST
def CadastroApi(request, form):
    if form.is_valid():
        User = CustomUser(
            username=form.cleaned_data['username'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            email=form.cleaned_data['email'],
            role=form.cleaned_data['role'],
        )
        User.set_password(form.cleaned_data['password'])
        User.save()

        messages.success(request,'Usuário cadastrado com sucesso!')

        form_login = forms.LoginForm()
        context = {
            'form': form_login,
        }

        return render(request, 'auth/login.html', context)


    # Por padrão, caso a API não consiga cadastrar o usuário, ela incluirá um erro no formulário e renderizará a view de cadastro
    form.add_error(None, 'Não foi possível realizar o cadastro, por favor verifique seus dados e tente novamente')
    context = {
        'form': form,
    }
    return render(request, 'auth/cadastro.html', context)


def LogoutApi(request):
    logout(request)
    return redirect(settings.LOGIN_URL)