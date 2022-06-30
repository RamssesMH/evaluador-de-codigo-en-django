#! /bin/bash
A=$(/bin/bash alumno.sh .txt)
echo -------------$A
if [[ $A == 10 ]]
then
    echo "hola a todos"
    exit 0
else
    exit 1
fi