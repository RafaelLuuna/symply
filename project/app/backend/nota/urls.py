from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.minhas_notas, name='minhas_notas'),
    path('cadastro/', views.cadastro, name='nota_cadastro'),
    path('cadastro/<int:id>', views.cadastro, name='nota_edit'),
    path('delete/<int:id>', views.delete, name='nota_delete'),
    path('info/<int:id>', views.info, name='nota_info'),
]