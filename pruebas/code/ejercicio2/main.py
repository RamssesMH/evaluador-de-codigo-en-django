import subprocess
import argparse
from unittest import result

def ejecutar_iniciar(script):
    iniciar = subprocess.Popen(['/bin/bash', script])
    try:
        outs, errs = iniciar.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        iniciar.kill()
        outs, errs = iniciar.communicate()
        return 0
    vari = iniciar.returncode

def ejecutar_comprobar(script, script_alumno):
    puntaje = 0
    comprobar = subprocess.Popen(['/bin/bash', script, script_alumno])
    try:
        outs, errs = comprobar.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        comprobar.kill()
        outs, errs = comprobar.communicate()
        return puntaje
    vari = comprobar.returncode
    if vari==0:
        puntaje=puntaje + 5
    return puntaje

def ejecutar_script_alumno(script):
    alumno = subprocess.Popen(['/bin/bash', script, 'prueba1', 'prueba2', 'prueba3'])
    try:
        outs, errs = alumno.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        alumno.kill()
        outs, errs = alumno.communicate()
        return 1
    return 0

if __name__ == '__main__':
    all_args =  argparse.ArgumentParser()
    all_args.add_argument("-i", "--Iniciar", help="script iniciar", required=True)
    all_args.add_argument("-p", "--Parametros", help="script parametros", required=True)
    all_args.add_argument("-c", "--Comprobar", help="script comprobar", required=True)
    all_args.add_argument("-a", "--Alumno", help="script alumno", required=True)
    
    args = vars(all_args.parse_args())

    script_iniciar = args['Iniciar']
    script_parametros = args['Parametros']
    script_comprobar = args['Comprobar']
    script_alumno = args['Alumno']
    puntaje = 0
    a = ejecutar_script_alumno(script_alumno)
    if a == 0:
        ejecutar_iniciar(script_iniciar)
        b = ejecutar_comprobar(script_parametros, script_alumno)
        if (b != 0):
            c =ejecutar_comprobar(script_comprobar, script_alumno)
            puntaje = b+c
    
    print (puntaje)