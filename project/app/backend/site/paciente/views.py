from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect


### VIEWS COMUNS ###
@require_http_methods(['GET','POST'])
@login_required
def index(request):
    return redirect('/home/')




@require_http_methods(['GET','POST'])
@login_required
def home(request):
    return render(request, 'site/home.html')





