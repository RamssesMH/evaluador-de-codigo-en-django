#!/usr/bin/env bash

function noHacerNada () {
    echo "No voy a terminar..."
}

function imprimirArchivo() {
    cat "señales.sh"
}

trap noHacerNada SIGINT SIGTERM
trap imprimirArchivo SIGILL

echo $$


while [ 1 -eq 1 ]; do
    sleep 1
done

