"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Default imports
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls


# Index View
from app.backend.site.views import index as index_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('', include('authentication.urls')),
    path('paciente/', include('app.backend.site.paciente.urls', namespace='paciente')),
    path('pscicologo/', include('app.backend.site.pscicologo.urls', namespace='pscicologo')),
] + debug_toolbar_urls()


if settings.DEBUG: # Essencial para desenvolvimento!
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)