#!/usr/bin/env bash

host="$1"
puerto="$2"
usuario="$3"

ssh -p "$puerto" "$usuario"@"$host" sleep 60; echo "hola mundo"
