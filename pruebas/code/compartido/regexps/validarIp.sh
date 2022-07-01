#!/usr/bin/env bash

function modo_uso() {
    echo "validarIp.sh ip"
    echo "Regresa \"válida\" si la ip sigue el formato de una ipv4, \"inválida de lo contrario\""
    echo "Parámetros:"
    echo "   ip: es una cadena que representa una ipv4"
    
}

[ "$1" ] || { modo_uso; exit 1; }


re1="25[0-5]"
re2="2[0-4][0-9]"
re3="1[0-9]{2}"
re4="[0-9]{1,2}"

reOcteto="(${re1})|(${re2})|(${re3})|(${re4})"

re="^((${reOcteto})\.){3}(${reOcteto})$"

ip="$1"

echo "$ip" | egrep "$re" > /dev/null && echo "válida" || { echo "inválida"; exit 1; }
