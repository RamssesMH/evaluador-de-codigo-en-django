#!/usr/bin/env bash

# modo de uso
# validaciones params

archivo_entrada="$1"

info_conexion=$(ccdecrypt -c "$archivo_entrada")

host=$(echo "$info_conexion" | cut -d , -f 1)
puerto=$(echo "$info_conexion" | cut -d , -f 2)
usuario=$(echo "$info_conexion" | cut -d , -f 3)
pass=$(echo "$info_conexion" | cut -d , -f 4)

export password="$pass"

./expect.exp "$host" "$puerto" "$usuario"
