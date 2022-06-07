from tkinter.tix import MAIN
from pip import main
import requests
import sys

token = '5561606760:AAE6Bk1j4_vo-lvR_AZ--8jWz9TL2lo_zSA'
chat_id = '1237694558'

def mandar_mensaje_bot(mensaje, token=token, chat_id=chat_id):
    send_text = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + mensaje
    response = requests.get(send_text)

if __name__ == '__main__':
    mensaje = sys.argv[1]
    mandar_mensaje_bot(mensaje)