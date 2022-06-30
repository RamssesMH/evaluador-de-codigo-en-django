#! /bin/bash
A=$(/bin/bash alumno.sh .txt)
if [[ $A == 10 ]]
then
    exit 0
else
    exit 1
fi 