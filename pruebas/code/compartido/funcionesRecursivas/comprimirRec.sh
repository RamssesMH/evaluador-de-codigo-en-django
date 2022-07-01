#!/usr/bin/env bash

function modo_uso() {
    echo "comprimirRec.sh ruta_directorio"
    echo "Comprime recursivamente sólo los archivos a partir"
    echo "del directorio de entrado, preserva estructura de directorio"
    echo "Parámetros:"
    echo "   ruta_directorio: ruta del directorio que representa la raíz del subárbol a procesar"
    echo "Ejemplo:"
    echo "comprimirRec.sh /tmp/algunDir"
}

function comprimir_archivos() {
    local directorio="$1"
    local nombre_comprimido="$2"
    separador=$IFS
    IFS=$(echo -en "\n\b")
    for archivo in $(ls "$directorio"); do
	if [ -f "$directorio/$archivo" ]; then
	    zip "$directorio/$nombre_comprimido" "$directorio/$archivo"
	    rm "$directorio/$archivo"
	fi
    done
    IFS=$separador
}

function comprimir_recursivamente() {
    local directorio_entrada="$1"
    local nombre_comprimido=$(basename "$directorio_entrada").zip
    comprimir_archivos "$directorio_entrada" "$nombre_comprimido"
    separador=$IFS
    IFS=$(echo -en "\n\b")
    for directorio in $(ls "$directorio_entrada"); do
	if [ -d "$directorio_entrada/$directorio" ]; then
	    comprimir_recursivamente "$directorio_entrada/$directorio"
	fi
    done
    IFS=$separador
}


[ "$1" ] && [ -d "$1" ] || { modo_uso; exit 1; }

comprimir_recursivamente "$1"

