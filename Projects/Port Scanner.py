import re
import socket
from unittest import result 
import threading
from queue import Queue

target = "192.168.91.8"
queue = Queue() # queue for list of port to test
open_ports = [] #list


def portscan(port):

    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #connection method 
        sock.connect((target, port)) #conn

        return True

    except:

        return False

def fill_queue(port_list): 
    for port in port_list:
        queue.put(port)  # fills queue with target ports

def worker():
    while not queue.empty():  # while queue is not empty
        port = queue.get() # get port from queue list
        if portscan(port):  # if port connects
            print("Port {} is open!".format(port)) #print this
            open_ports.append(port)  #add port to open_ports list

port_list = range(79, 81) #test from 1-1024
fill_queue(port_list) #fill port_list

thread_list = []

for t in range(10):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open Ports Are: ", open_ports) #prints open_ports list 