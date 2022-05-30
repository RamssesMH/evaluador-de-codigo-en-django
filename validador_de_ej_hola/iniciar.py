import os
import sys
entradas= "./entradas_prueba.txt"
with open(entradas,"r") as archivo:
    for entrada in archivo:
        salida_esperada="hola "+entrada.rstrip()

        lista= [ar for ar in os.listdir('.') if ar.endswith('sh')]

        vari= os.system("./"+lista[0]+" "+entrada)
        if vari != 0:
            sys.exit(1)