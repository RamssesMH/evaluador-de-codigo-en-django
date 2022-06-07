#!/usr/bin/env bash

[[ -f "$1" ]] || { echo "Se esperaba un archivo cifrado con variables de entorno"; exit 1; }


for linea in $(ccdecrypt -c "$1"); do
    export "$linea"
done


docker-compose up -d
