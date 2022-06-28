import os
import subprocess

entradas= "./entradas_prueba.txt"

if os.path.exists(entradas):
    if os.path.isfile(entradas):
        print("archivo correcto")
    else:
        print("el archivo no es el esperado")
else:
    print("El archivo no existe")