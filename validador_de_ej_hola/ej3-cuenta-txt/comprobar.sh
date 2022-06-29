#! /bin/bash
A=$(/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej3-cuenta-txt/alumno.sh .txt)
echo -------------$A
if [[ $A == 10 ]]
then
    echo "hola a todos"
    exit 0
else
    exit 1
fi