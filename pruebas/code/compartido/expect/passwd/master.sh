#!/usr/bin/env bash

arch_servidores="$1"
usuario="$2"
pass_viejo="$3"
pass_nuevo="$4"

# función de modo de uso va acá

# Validaciones de parámentros acá

for servidor in $(cat "$arch_servidores"); do
    ./procesarServidor.exp "$servidor" "$usuario" "$pass_viejo" "$pass_nuevo"
done
