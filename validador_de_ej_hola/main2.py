import subprocess
import os
bien=0
mal=0
vari=os.system("python3 /home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/ejecucion.py")
if vari==0:
   bien=1
else:
    mal=1

vari=os.system("python3 /home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/parametros.py")
if vari==0:
   bien=1
else:
    mal=1

vari=os.system("python3 /home/ramsses/psegura/proyectoPrograSegura/validador_de_ej_hola/ej2-imprime-archivo/evaluacion.py")
if vari==0:
   bien=1
else:
    mal=1
