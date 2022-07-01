#! /bin/bash
/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/alumno.sh /home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/sdfdsgsh
if [[ $? == 0 ]]
then
    echo 0
else
    echo 1
    exit 1
fi

/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/alumno.sh /home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/asf.txt
if [[ $? == 0 ]]
then
    echo 0
else
    echo 1
    exit 1
fi

/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/alumno.sh /home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/nombrearchivo.txt


if [[ $? == 0 ]]
then
    echo 0
    exit 0
else
    echo 1
    exit 1
fi