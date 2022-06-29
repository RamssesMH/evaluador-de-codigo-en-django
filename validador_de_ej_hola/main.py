import subprocess
import os
import sys
bien=0
mal=0
carpeta= sys.argv[1]

vari=os.system("/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/"+carpeta+"/iniciar.sh")
if vari==0:
   bien=bien + 3.3
else:
    mal=1

vari=os.system("/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/"+carpeta+"/parametros.sh")
if vari==0:
   bien=bien + 3.3
else:
    mal=1

vari=os.system("/home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/"+carpeta+"/comprobar.sh")
if vari==0:
   bien=bien + 3.3
else:
    mal=1
print(round(bien))