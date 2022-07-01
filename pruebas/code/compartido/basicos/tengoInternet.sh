#!/usr/bin/env bash

# Mientras no tenga internet
while ! curl https://www.google.com &> /dev/null; do
    echo "No tienes internet";
    sleep 5;
done

echo "Ya tines internet!!!";
