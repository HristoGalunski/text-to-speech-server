#taskkill /IM executablename
import sys
from socket import socket, AF_INET, SOCK_DGRAM
import time


if __name__ == "__main__":
        SERVER_IP   = '?'
        PORT_NUMBER = 5001
        SIZE = 1024
        print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

        mySocket = socket(AF_INET, SOCK_DGRAM)

        while True:
                #Start message with '`' for a 20 second delay, send 'exit' to quit
                message = input()
                if(message[0] == "`") :
                        time.sleep(20)
                        mySocket.sendto(bytes(message[1:], encoding='utf-8'),(SERVER_IP, PORT_NUMBER))
                else:
                        mySocket.sendto(bytes(message, encoding='utf-8'),(SERVER_IP, PORT_NUMBER))
                print("sent")

        sys.exit()
