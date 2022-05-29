import subprocess
import os

entrada="usuario"
salida_esperada="hola usuario"
lista= [ar for ar in os.listdir('.') if ar.endswith('sh')]
# print (lista[0])
comando_entrada=["./"+lista[0], entrada]
# print (comando_entrada)

salida= subprocess.Popen(comando_entrada, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = salida.communicate()
salida_final= stdout.decode('utf-8').strip()
salida_final= salida_final.lower()
if salida_final==salida_esperada:
    print("Buen programa")
else:
    print ("tu programa tiene un error")