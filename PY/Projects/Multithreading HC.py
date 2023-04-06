import queue
import threading
import os
from queue import Queue
from traceback import print_stack
import socket
from xmlrpc.client import ProtocolError


ip = input("Enter an IP to run the healthcheck on: ")# 'ip' will be taken in as an input


def P80(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = (ip,port)
    result = sock.connect_ex(host)

    if result == 0:
        print("Port 80 Is Open")
    else:
        print("Port 80 Is Not Open")

def P443(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = (ip,port)
    result = sock.connect_ex(host)

    if result == 0:
        print("Port 443 Is Open")
    else:
        print("Port 443 Is Not Open")



if __name__ == "__main__":
        t1 = threading.Thread(target=P80, args=(80,))
        t2 = threading.Thread(target=P443, args=(443,))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

      
