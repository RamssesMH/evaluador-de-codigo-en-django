#! /bin/bash
bash $1 sdfdsgsh
if [[ $? == 0 ]]
then
    echo 0
else
    echo 1
    exit 1
fi

bash $1 asf.txt
if [[ $? == 0 ]]
then
    echo 0
else
    echo 1
    exit 1
fi

bash $1 nombrearchivo.txt


if [[ $? == 0 ]]
then
    echo 0
    exit 0
else
    echo 1
    exit 1
fi