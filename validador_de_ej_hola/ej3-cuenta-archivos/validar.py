import subprocess
import os
bien=0
mal=0
vari=os.system("python3 iniciar.py")
if vari==0:
    vari2=os.system("python3 parametros.py")
    if vari2==0:
        with open("./entradas_prueba.txt","r") as archivo:
            for entrada in archivo:
                cadena_sin_salto_de_linea = entrada.rstrip()
                lista2= [ar for ar in os.listdir('.') if ar.endswith(cadena_sin_salto_de_linea)]
                salida_esperada = len(lista2)
                lista= [ar for ar in os.listdir('.') if ar.endswith('sh')]
                # print (lista[0])
                comando_entrada=["./"+lista[0], entrada]
                # print (comando_entrada)

                salida= subprocess.Popen(comando_entrada, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = salida.communicate()
                salida_final= stdout.decode('utf-8').strip()
                salida_final= salida_final.lower()
                parseo = str(salida_esperada)
                if salida_final==parseo:
                    print("hola")
                    bien= bien + 1
                else:
                    print("adios")
                    mal= mal + 1

        if bien>2:
            print("Aprobaste")
        else:

            print("Reprobaste")
    else:
        print("tu programa no pasó la segunda etapa")
else:
    print("tu programa no pasó la primera etapa")