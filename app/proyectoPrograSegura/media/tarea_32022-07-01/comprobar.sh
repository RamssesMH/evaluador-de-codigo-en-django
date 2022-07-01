#! /bin/bash
A=$(bash $1 nombrearchivo.txt)
if [[ $A == "salida final" ]]
then
    exit 0
else
    echo 1
    exit 1
fi