% prepara el repositorio para su despliegue. 
release: sh -c 'cd innosoftFinanzas && python manage.py migrate --noinput'
% especifica el comando para lanzar Innosoft
web: gunicorn innosoftFinanzas.wsgi:application --log-file -