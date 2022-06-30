#! /bin/bash
/bin/bash alumno.sh txt
if [[ $? == 0 ]]
then
    exit 0
else
    exit 1
fi 