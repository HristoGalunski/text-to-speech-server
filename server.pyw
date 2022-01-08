from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
import ssl
import winsound
import time
from gtts import gTTS
import os


if __name__ == "__main__":
        PORT_NUMBER = 5000
        SIZE = 2048

        hostName = gethostbyname( "0.0.0.0" )

        mySocket = socket(AF_INET, SOCK_DGRAM)
        mySocket.bind((hostName, PORT_NUMBER))

        print ("Test server listening on port {0}\n".format(PORT_NUMBER))

        def save_and_play(text):
                language = 'en'
                myobj = gTTS(text=str(data), lang=language, slow=False)
                myobj.save("dks4.wav")
                winsound.PlaySound('dks4.wav', winsound.SND_FILENAME)

        while True:
                (data,addr) = mySocket.recvfrom(SIZE)
                if(str(data) == 'exit'):
                        quit()
                save_and_play(data)
                time.sleep(3)
        sys.ext()
