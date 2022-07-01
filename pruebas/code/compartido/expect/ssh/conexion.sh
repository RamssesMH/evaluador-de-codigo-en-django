#!/usr/bin/env bash

usuario="$1"
host="$2"
puerto="$3"

ssh -p "$puerto" "$usuario"@"$host" echo "hola mundo"
