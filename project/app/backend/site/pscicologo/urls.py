from django.urls import path, include
from . import views

app_name = 'pscicologo'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('nota/', include('app.backend.nota.urls')),
]