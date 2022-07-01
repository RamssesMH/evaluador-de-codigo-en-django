import subprocess
import argparse
from unittest import result

def ejecutar_iniciar(script):
    bien = 0
    iniciar = subprocess.Popen(['/bin/bash', script])
    try:
        outs, errs = iniciar.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        iniciar.kill()
        outs, errs = iniciar.communicate()
        print ('0')
        exit(1)
    vari = iniciar.returncode
    if vari==0:
        bien=bien + 3.3
    return bien

def ejecutar_parametros(script):
    bien = 0
    parametros = subprocess.Popen(['/bin/bash', script])
    try:
        outs, errs = parametros.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        parametros.kill()
        outs, errs = parametros.communicate()
        print ('0')
        exit(1)
    vari = parametros.returncode
    if vari==0:
        bien=bien + 3.3
    return bien

def ejecutar_comprobar(script):
    bien = 0
    comprobar = subprocess.Popen(['/bin/bash', script])
    try:
        outs, errs = comprobar.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        comprobar.kill()
        outs, errs = comprobar.communicate()
        print ('0')
        exit(1)
    vari = comprobar.returncode
    if vari==0:
        bien=bien + 3.3
    return bien

if __name__ == '__main__':
    all_args =  argparse.ArgumentParser()
    all_args.add_argument("-i", "--Iniciar", help="script iniciar", required=True)
    all_args.add_argument("-p", "--Parametros", help="script parametros", required=True)
    all_args.add_argument("-c", "--Comprobar", help="script comprobar", required=True)
    
    args = vars(all_args.parse_args())

    script_iniciar = args['Iniciar']
    script_parametros = args['Parametros']
    script_comprobar = args['Comprobar']
    bien = 0
    a = ejecutar_iniciar(script_iniciar)
    b = ejecutar_parametros(script_parametros)
    c =ejecutar_comprobar(script_comprobar)
    
    result = a+b+c
    
    print (round(result))