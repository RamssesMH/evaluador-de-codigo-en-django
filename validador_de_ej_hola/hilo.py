from pickle import TRUE
import threading
import time

def contar():
    '''Contar hasta cien'''
    time.sleep(2)
    print
    print("tiempo terminado")
    exit()
hilo1 = threading.Thread(target=contar)
hilo1.start()
i=0
while True:
    i=i+1
