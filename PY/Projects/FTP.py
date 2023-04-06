import ftplib
import os
#ftp = ftplib.FTP()
host = "192.168.91.8"
#port = 21
#ftp.connect(host, port)
#print (ftp.getwelcome())

print("FTP Login to", host)

uname = input("Enter your username: ")
passwd = input("Enter your Password: ") 
try:
      print ("Logging in...")
      session = ftplib.FTP(host, uname, passwd)
      #session = ftp.login(uname, passwd)
      os.system('cls')
except:
    print("failed to login") 

try:
      fileN = input ("Enter file to upload: ")
      file = open(fileN, 'rb')
except:
    print("failed to open file")

try:
    session.storbinary('STOR ' + fileN, file)
except:
    print("failed to upload file")

try:
    file.close()
except:
    print("failed to login")

session.quit()


