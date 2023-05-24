from cgitb import reset
from ctypes.wintypes import tagRECT
import os
import queue 
import socket
from unittest import result
import threading
from queue import Queue




# PING SECTION
hosts = [] #list of IP's that will be pinged
port_list = (80) # 


ip = input("Enter an IP to run the healthcheck on: ") # 'ip' will be taken in and added to list
hosts.append(ip) # added to list

for host in hosts: #first element in hosts to take in as 'host'
    os.system('ping ' + host) # runs'ping' + selected ip from the list

# PORT SECTION

target = host 
queue = Queue() # queue for list of ports to test
open_ports = [] # list of open ports

def portscan(port):

    try:

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #connection method
        sock.connect((target, port)) #scan connection

        return True

    except: 

        return False

def fill_queue(port_list):
    for port in port_list:
        queue.put(port) #adds port to the queue 

def worker():
    while not queue.empty(): # while queue is not empty
        port = queue.get() # get port from list
        if portscan(port): #if port connects 
            print("port {} is open!".format(port)) #outputs
            open_ports.append(port) # adds open port to list


fill_queue(port_list) # adds next port in port_list to queue 

thread_list =[]

for t in range(1):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

    for thread in thread_list:19
    thread.start()
    for thread in thread_list:
        thread.join()


print("Open Ports: ", open_ports) # prints out all open ports list









