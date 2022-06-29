#! /bin/bash
/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej3-cuenta-txt/alumno.sh txt
if [[ $? == 0 ]]
then
    exit 0
else
    exit 1
fi