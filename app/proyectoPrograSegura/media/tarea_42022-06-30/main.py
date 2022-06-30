import subprocess

hijo = subprocess.Popen(['/bin/bash', 'iniciar.sh'])
try:
    outs, errs = hijo.communicate(timeout=10)
except subprocess.TimeoutExpired:
    print("Tiempo excedido")
    hijo.kill()
    outs, errs = hijo.communicate()

hijo2 = subprocess.Popen(['/bin/bash', 'parametros.sh'])
try:
    outs, errs = hijo2.communicate(timeout=10)
except subprocess.TimeoutExpired:
    print("Tiempo excedido")
    hijo2.kill()
    outs, errs = hijo2.communicate()

hijo3 = subprocess.Popen(['/bin/bash', 'iniciar.sh'])
try:
    outs, errs = hijo3.communicate(timeout=10)
except subprocess.TimeoutExpired:
    print("Tiempo excedido")
    hijo3.kill()
    outs, errs = hijo3.communicate()

print ("prueba")