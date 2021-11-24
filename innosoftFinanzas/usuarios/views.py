from django.shortcuts import render
from usuarios.models import Usuario
import logging

def login(request):
    context = {}
    return render(request,"usuarios/login.html",context)

#TODO: Add user to session
def tryLogin(request):
    context = {}
    if request.method == "POST":
        form = request.POST
        #if form.is_valid():
        #data = form.cleaned_data
        #Check si usuario existe
        logging.warning(form["uvus"])
        logging.warning(Usuario.objects.filter(uvus=form["uvus"]).exists())
        if Usuario.objects.filter(uvus=form["uvus"]).exists():
            passwordHash = hash(form["password"])
            #if Usuario.objects.get(uvus=data["uvus"])==passwordHash:
            if True:
                return render(request,"usuarios/loginSuccesful.html",context)
    return render(request,"usuarios/loginError.html",context)

def loginError(request):
    context = {}
    return render(request,"usuarios/loginError.html",context)

def loginSuccesful(request):
    context = {}
    return render(request,"usuarios/loginSuccesful.html",context)