#!/usr/bin/env bash

function modo_uso() {
    echo "borrarRec.sh directorio"
    echo "Borra recursivamente archivos con extensión .txt, a partir de directorio"
    echo "Paramétros:"
    echo "   directorio: es el path de un directorio"
    echo "Ejemplo:"
    echo "   borrarRec.sh /tmp"
}


function borrar_txts() {
    local dir="$1"
    separador=$IFS
    IFS=$(echo -en "\n\b")
    for archivo in $(ls -a "$dir" | egrep "\.txt$"); do
	[ -f "$dir/$archivo" ] && rm "$dir/$archivo"
    done
    IFS=$separador
}

function borrar_rec() {
    local entrada="$1"
    borrar_txts "$entrada"
    separador=$IFS
    IFS=$(echo -en "\n\b")
    for directorio in $(ls -A "$entrada"); do
	if [ -d "$entrada/$directorio" ]; then
	    borrar_rec "$entrada/$directorio"
	fi
    done
    IFS=$separador
}


[ -d "$1" ] || { modo_uso; exit 1; }

borrar_rec "$1"
