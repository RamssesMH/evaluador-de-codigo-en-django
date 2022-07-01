#! /bin/bash
[ -f "$1" ]  || { exit 1; }

bash $1 archivo1.txt archivo2.txt salida.txt
bash $1 archivo1.txt archivo2.txt salida1.txt
if [ $? == 0 ]
then
    diff salida.txt salida1.txt
    if [ $? == 0 ] 
    then
        exit 0
    else
        exit 1
    fi
else
    exit 1
fi