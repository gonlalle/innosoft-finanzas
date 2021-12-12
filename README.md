Pip version: 20.0.2
Django version: 3.2.8
python version: 3.8.10

Session handling:
In order to see the user's permision, in the views.py  access to request.session["session"], it will return a string of the following form: 
NA: nada
MB: miembro
CD: coordinador
PR: profesor
SU: superuser
Cada permiso tiene un cierto nivel de acceso.

#Working with static files (css, js...):
Add a cs/js/... folder in the module you are working (ie: if working in inventario, add a folder "css" with a file "style.css"). To access to the static file do:
{% load static %}
{% static 'js/adminUsuarios.js' %}

ie:
{% load static %}
<link rel="stylesheet" href="{% static 'inventario/css/style.css' %}">