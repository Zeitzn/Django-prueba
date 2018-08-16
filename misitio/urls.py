"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from misitio.views import hola,raiz,fecha_actual,horas_adelante
from contacto.views import contactos
from biblioteca import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',raiz),
    path('hola/',hola),
    path('fecha/',fecha_actual),
    path('fecha/mas/<int:offset>/',horas_adelante),
    path('formulario-buscar/',views.formulario_buscar),
    path('buscar/',views.buscar),
    path('contactos/',contactos)
]
