import socket

hostname = socket.gethostname()  #gets hostname
IPAddr = socket.gethostbyname(hostname) #gets ip addr

print("your computer name is: " + hostname)
print("Your computer IP address is: " + IPAddr)



