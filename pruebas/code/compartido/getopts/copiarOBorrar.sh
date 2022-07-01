#!/usr/bin/env bash

opcionR=""
opcionC=""
paramR=""
paramC=""

function modoUso() {
    echo "copiarOBorrar OPCIONES [path_destino]";
    echo "Este script copia o borra un archivo dado";
    echo "OPCIONES:";
    echo "   -c archivo: copia el archivo";
    echo "   -r archivo: borra el archivo";
    echo "Parámetros posicionales:";
    echo "   path_destino: sólo necesario con la opción -c, establece el destino de la copia"
}


while getopts ":c:r:" opt; do
    case $opt in
	c)
	    opcionC="1";
	    paramC="$OPTARG";
	    ;;
	r)
	    opcionR="1";
	    paramR="$OPTARG";
	    ;;
	"?")
	    echo "Opción inválida -$OPTARG";
	    modoUso;
	    exit 1;
	    ;;
	:)
	    echo "Se esperaba un parámetro en -$OPTARG";
	    modoUso;
	    exit 1;
	    ;;
    esac
done

#echo $OPTIND
shift $((OPTIND-1)) #borrar to1dos los params que ya procesó getopts



# Revisión de errores

# Revisar que no se hayan activado las dos opciones al mismo tiempo
[ ! -z "$opcionR" ] && [ ! -z "$opcionC" ] && { echo "No se pueden activar las dos opciones al mismo tiempo"; modoUso; exit 1; }

# Revisar que se haya pasado al menos una opción
[ ! -z "$opcionR" ] || [ ! -z "$opcionC" ] || { echo "Debiste activar al menos una opción"; modoUso; exit 1; }

# Revisar que haya un parámetro posicional asociado cuando se usa -c
[ ! -z "$opcionC" ] && [ -z "$1" ] &&  { echo "Se debe pasar un parámetro posicional con la opción -c"; modoUso; exit 1; }

if [ ! -z "$opcionC" ]; then
    cp "$paramC" "$1";
elif [ ! -z "$opcionR" ]; then
    rm "$paramR"
fi
