import threading


option = input("Would you like to square or halve? ")

num = int(input("Enter a number to use for this operation ")) # takes input to use as argument



def square(num): #function to square a number
    print("Square: {}" .format(num * num * num))
def halve(num): # function to halve a number
    print("Halve: {}" .format(num / 2))

if __name__ =="__main__":
    #creating thread
    thread1 = threading.Thread(target=square, args=(num,))
    thread2 = threading.Thread(target=halve, args=(num,))


if option == "square":
    thread1.start() #start thread 1
    thread1.join() #join thread 1

else:
    thread2.start() #start thread 2
    thread2.join() #join thread 2


# Both thread should of stopped by now !

print("Done!")


