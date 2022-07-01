#!/usr/bin/env bash

usuario="$1"
host="$2"

ssh "$usuario"@"$host" passwd
