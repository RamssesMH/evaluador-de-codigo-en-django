import subprocess
import os
bien=0
mal=0
vari=os.system("python3 iniciar.py")
if vari==0:
    with open("./entradas_prueba.txt","r") as archivo:
        for entrada in archivo:
            salida_esperada="hola "+entrada.rstrip()

            lista= [ar for ar in os.listdir('.') if ar.endswith('sh')]
            # print (lista[0])
            comando_entrada=["./"+lista[0], entrada]
            # print (comando_entrada)

            salida= subprocess.Popen(comando_entrada, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = salida.communicate()
            salida_final= stdout.decode('utf-8').strip()
            salida_final= salida_final.lower()
            if salida_final==salida_esperada:
                bien= bien + 1
            else:
                mal= mal + 1

    if bien>5:
        print("Aprobaste tienes ", bien ," de 10")
    else:
        print("Reprobaste tienes ", bien ," de 10")
else:
    print("tu programa no pasó la primera etapa")