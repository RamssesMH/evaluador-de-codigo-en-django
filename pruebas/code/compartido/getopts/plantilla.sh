#!/usr/bin/env bash

opcionB=""
opcionA=""
paramA=""

while getopts ":a:b" opt; do
    case $opt in
	a)
	    opcionA="1";
	    echo "Activaste opción a";
	    echo "su parámetro es $OPTARG";
	    paramA="$OPTARG"
	    echo "";
	    ;;
	b)
	    echo "Activaste opción b";
	    opcionB="1";
	    echo "";
	    ;;
	"?")
	    echo "Opción inválida -$OPTARG";
	    exit 1;
	    ;;
	:)
	    echo "Se esperaba un parámetro en -$OPTARG";
	    exit 1;
	    ;;
    esac
done

#echo $OPTIND
shift $((OPTIND-1)) #borrar to1dos los params que ya procesó getopts

[ "$opcionA" ] || { echo "la opción -a es obligatoria"; exit 1; }

echo "Resto de parámetros: $@"
