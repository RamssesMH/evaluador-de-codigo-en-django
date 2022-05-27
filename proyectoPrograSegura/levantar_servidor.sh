#! /bin/bash
[[ -f "$1" ]] || { echo "Se esperaba un archivo con variables de entorno"; exit 1; }

for linea in $(ccdecrypt -c $1); do
    export "$linea"
done

python3 manage.py migrate
python3 manage.py makemigrations
python3 manage.py runserver 0.0.0.0:8000