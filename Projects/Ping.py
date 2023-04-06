import os

hosts = []

ip = input("Enter an ip:")  #takes input
hosts.append(ip) #puts input into list of hosts

for host in hosts: # takes an item from host and adds to loop 
    os.system('ping ' + host) # 'runs' ping + host picked from loop statement
    

    