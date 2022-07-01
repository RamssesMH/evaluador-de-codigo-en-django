#! /bin/bash
[ -f "$1" ]  || { exit 1; }
# Ejecutar sin parámetros
bash $1 >& log
# Si falla, es correcto
if [[ $? == 1 ]]
then
    # Ejecutar con un parámetro
    bash $1 archivo1.txt >& log
    # Si falla, es correcto
    if [[ $? == 1 ]]
    then
        # Ejecutar con dos parámetros
        bash $1 archivo1.txt archivo2.txt >& dosparametros
        cat dosparametros | grep $1":" >& log
        if [[ $? == 1 ]]
        then
            #Ejecutar con archivos que no existen
            bash $1 respaldar.sh tengoInternet.sh resultado.tmp >& log
            #Verifica que el archivo resultado.tmp no se haya creado
            cat resultado.tmp >& log
            if [[ $? == 1 ]]
            then
                #Comprobar que el última parámetro es un archivo en un directorio válido
                bash $1 archivo1.txt archivo2.txt /comporersda/resuasda.tx >& error
                # Verificar que el error del tercer parámetro no sea el que arroja el sistema, sino el alumno
                cat error | grep $1":"
                if [[ $? == 0 ]]
                then
                    exit 1
                else
                    exit 0
                fi
            else
                exit 1
            fi
        else
            exit 1
        fi
    else
        exit 1
    fi
else
    exit 1
fi