import logging
from django.shortcuts import render

from usuarios.models import Usuario

def index(request):
    context = {}
    if checkCredentials(request):
        return render(request,"administrador/index.html",context)
    else:
        return handleInvalidEntry(request,context)

def checkCredentials(request):
    logging.warn(request.session["session"])
    if "session" in request.session and request.session["session"]!="NA" and request.session["session"]!="MB":
        return True
    else:
        return False

def usuarios(request):
    context = {"usuarios":Usuario.objects.all}
    return render(request,"administrador/adminUsuarios.html",context)

def handleInvalidEntry(request,context):
    return render(request,"index.html",context)