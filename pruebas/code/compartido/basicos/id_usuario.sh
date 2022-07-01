#!/usr/bin/env bash

usuario_actual=$(whoami)
cat /etc/passwd | grep "$usuario_actual" | cut -d : -f 3
