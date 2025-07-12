from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.urls import reverse


### VIEWS COMUNS ###
@require_http_methods(['GET','POST'])
@login_required
def index(request):
    return redirect(reverse('home'))



