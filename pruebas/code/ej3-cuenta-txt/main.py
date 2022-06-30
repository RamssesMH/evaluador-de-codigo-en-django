import subprocess
import argparse


def ejecutar_iniciar(script):
    iniciar = subprocess.Popen(['/bin/bash', script])
    try:
        outs, errs = iniciar.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        iniciar.kill()
        outs, errs = iniciar.communicate()
        exit(1)

def ejecutar_parametros(script):
    parametros = subprocess.Popen(['/bin/bash', script])
    try:
        outs, errs = parametros.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        parametros.kill()
        outs, errs = parametros.communicate()
        exit(1)

def ejecutar_comprobar(script):
    comprobar = subprocess.Popen(['/bin/bash', script])
    try:
        outs, errs = comprobar.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        comprobar.kill()
        outs, errs = comprobar.communicate()
        exit(1)

if __name__ == '__main__':
    all_args =  argparse.ArgumentParser()
    all_args.add_argument("-i", "--Iniciar", help="script iniciar", required=True)
    all_args.add_argument("-p", "--Parametros", help="script parametros", required=True)
    all_args.add_argument("-c", "--Comprobar", help="script comprobar", required=True)
    
    args = vars(all_args.parse_args())

    script_iniciar = args['Iniciar']
    script_parametros = args['Parametros']
    script_comprobar = args['Comprobar']

    ejecutar_iniciar(script_iniciar)
    ejecutar_parametros(script_parametros)
    ejecutar_comprobar(script_comprobar)