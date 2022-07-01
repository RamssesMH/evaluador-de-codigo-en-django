#!/usr/bin/env bash

function modo_uso() {
    echo "Modo de uso:"
    echo "tieneCadena.sh directorio cadena";
    echo "Regresa el nombre de los archivos en directorio, que contengan la cadena"
    echo "  - directorio: es la ruta de un directorio válido"
    echo "  - cadena: es la cadena a buscar en los archivos"
    echo "Ejemplo:"
    echo "tieneCadena.sh /tmp ejemplo"
}

[ "$2" ] || { echo "Se esperaban dos parámetros"; modo_uso; exit 1; }
[ -d "$1" ] || { echo "El primer parámetro debe ser un directorio"; modo_uso; exit 1; }

path_entrada="$1";
cadena="$2";

separador=$IFS;
IFS=$(echo -en "\n\b"); # solo considerar \n como separador

for archivo in $(ls "$path_entrada"); do
    if [ -f "$path_entrada/$archivo" ]; then
	if cat "$path_entrada/$archivo" | grep "$cadena" &> /dev/null; then
	    echo "$archivo";
	fi
    fi
done

IFS=$separador
