"""innosoftFinanzas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include

from . import views
from usuarios import views as usuariosViews
from administrador import views as adminViews

#Comentar en mayusculas el módulo al que se refiere la url

urlpatterns = [
    path('',views.index),
    path('superadmin/', admin.site.urls),
    #USUARIOS
    #Login
    path('login/', usuariosViews.login, name="login"),
    path('handlelogin/', usuariosViews.handleLogin, name="handleLogin"),
    path('loginerror/', usuariosViews.loginError),
    path('loginsucces/', usuariosViews.loginSuccesful),
    #Register
    path('register/', usuariosViews.register, name="register"),
    path('handleregistration/', usuariosViews.handleRegistration, name="handleRegistration"),
    #ADMINISTRADOR
    path("admin/", adminViews.index, name="adminIndex"),
    path("admin/usuarios", adminViews.usuarios, name="adminUsuarios"),
]
