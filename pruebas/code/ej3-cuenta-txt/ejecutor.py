from base64 import decode
import subprocess
import base64

iniciar = subprocess.run(['docker', 'run', '--name', '25-7', '-it', '25-7', 'main.py', '-i', 'iniciar.sh', '-p', 'parametros.sh', '-c' 'comprobar.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# try:
#     outs, errs = iniciar.communicate(timeout=5)
# except subprocess.TimeoutExpired:
#     iniciar.kill()
#     outs, errs = iniciar.communicate()
# salida = outs.decode('utf-8')
print(iniciar)
# b = subprocess.Popen(['docker', 'rm', '23-7'], stdout=subprocess.PIPE)
# try:
#     outs, errs = b.communicate(timeout=5)
# except subprocess.TimeoutExpired:
#     b.kill()
#     outs, errs = b.communicate()
