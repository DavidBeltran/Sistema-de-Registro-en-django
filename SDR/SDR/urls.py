"""SDR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, patterns, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [

    url(r'^$', views.index, name='login'),
    url(r'^validar-login$', views.validarLogin, name='validar-login'),
    url(r'^menu$', views.menu, name='menu'),
    url(r'^cerrar-sesion$', views.closeSession, name='cerrar sesion'),
    url(r'^menu/nuevo-usuario$', views.newUser, name='nuevo usuario'),
    url(r'^menu/actualizar-usuario$', views.updateUSer, name='actualizar usuario'),
    url(r'^menu/buscar-usuario$', views.searchUser, name='buscar usuario'),
    url(r'^menu/tabla-usuario$', views.searchUserTable, name='tabla usuario'),
    url(r'^saveUser$', views.saveUser, name='guardar usuario'),
    url(r'^roles$', views.changeRoles, name='cargar roles'),

] + static(settings.STATIC_URL)
