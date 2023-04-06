def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y


print("Select An Operator: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice 1-4: ")

# if choice is valid it continues
    if choice in('1','2','3','4'):

#takes in numbers as floats
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))


#does all operations 
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        if choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        if choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        if choice == '1':
            print(num1, "/", num2, "=", divide(num1, num2))


        next_calculation = input("Let's do another calculation(Y/N) ")

        if next_calculation == "N" or "n":
          break
        
            

else:
    print("Invalid Input ")