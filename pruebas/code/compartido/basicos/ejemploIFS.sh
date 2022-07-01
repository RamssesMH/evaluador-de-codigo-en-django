#!/usr/bin/env bash

directorio="/tmp/prueba"

separador=$IFS
IFS=$(echo -en "\n\b") # solo considerar \n como separador

for archivo in $(ls "$directorio"); do
    cp "$directorio/$archivo" /tmp
    #echo "$archivo"
done

IFS=$separador
