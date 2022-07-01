#!/usr/bin/env bash

timeout=60
cadena_ok="ready for connections"
tiempo1=$(date +"%s")
sudo systemctl start mysqld &
echo "Esperando a que se levante mysql..."
while ! sudo systemctl status mysql | egrep "$cadena_ok" > /dev/null; do
    echo "esperando..."
    sleep 2
    tiempo2=$(date +"%s")
    let dif=tiempo2-tiempo1
    [ $dif -gt $timeout ] && { echo "Tiempo de espera exedido"; exit 1; }
done

echo "Se inició el servicio"

