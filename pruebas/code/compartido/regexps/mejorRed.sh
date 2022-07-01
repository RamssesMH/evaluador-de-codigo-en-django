#!/usr/bin/env bash

# Terminar este script de tarea...

lista_valores=( $(iwlist wlp8s0f3u3 scanning | grep -oP "(Quality=\K[0-9]{1,2})") )
lista_essids=( $(iwlist wlp8s0f3u3 scanning | grep -oP "(ESSID:\K".*")") )

echo "${#lista_essids[@]}" 
