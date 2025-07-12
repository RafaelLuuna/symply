from django.urls import path, include
from . import views as auth_views

urlpatterns = [
    path('login/', auth_views.login, name='login'),
    path('cadastro/', auth_views.cadastro, name='cadastro'),
    path('logout/', auth_views.logout, name='logout')
]