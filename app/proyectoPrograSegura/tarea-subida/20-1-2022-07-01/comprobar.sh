#! /bin/bash
A=$(/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/alumno.sh /home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/nombrearchivo.txt)
if [[ $A == "salida final" ]]
then
    exit 0
else
    echo 1
    exit 1
fi