#! /bin/bash
contador=1
contadors=10
while [ $contadors -ge $contador ]
do
    touch archivo$contador.txt
    let contador=$contador+1
done