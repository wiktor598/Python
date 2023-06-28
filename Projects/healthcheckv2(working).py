import os
from queue import Queue
import socket
import threading

hosts = []
port_list = [9080, 9443,]
open_ports = []



ip = input("What Appliance would you like to run the HC on ? \n")

for ip in hosts:
    os.system('ping' + ip)

target = ip
queue = Queue()



def portscan(port):

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    
def fill_q(port_list):
    for port in port_list:
        queue.put(port)
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open ".format(port))
            open_ports.append(port)

fill_q(port_list)

thread_list = []

for t in range(1):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

    for thread in thread_list:19
    thread.start()
    for thread in thread_list:
        thread.join()

print("Open Ports {}".format(open_ports))

