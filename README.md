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

