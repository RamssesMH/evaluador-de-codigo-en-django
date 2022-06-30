#! /bin/bash
A=$(/bin/bash alumno.sh nombrearchivo.txt)
if [[ $A == "salida final" ]]
then
    exit 0
else
    echo 1
    exit 1
fi