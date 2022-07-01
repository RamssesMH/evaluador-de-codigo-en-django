#!/usr/bin/env bash

[ "$3" ] ||  { echo "No pasaste tres parámetros"; exit 1; }
[ -f "$1" ] && [ -f "$2" ]  ||
    { echo "Los dos primeros argumentos deben ser un archivo que existe"; exit 1; }
[ -d $(dirname "$3" ) ] || { echo "el tercer parámetro debe ser un archivo situado en un directorio que exista"; exit 1; }


archivo1="$1"
archivo2="$2"
salida="$3"

cat "$archivo1" > "$salida"
cat "$archivo2" >> "$salida"