import re  



def validate_password(password):  
    if len(password) < 8:  #if the length of the password is less than 8 return false
        return False  
    if not re.search("[a-z]", password):  #if the password does not contain atleast one lowercase return false 
        return False  
    if not re.search("[A-Z]", password):  #if the password does not contain atleast one uppercase return false 
        return False  
    if not re.search("[0-9]", password):  #if the password does not contain atleast one integer return false 
        return False  
    return True   # otherwise return true 
  

password = input("Enter your password ") # takes password as input

if validate_password(password):  # if valid_password returns true to the password argument then print "Valid Password"
    print("Valid password")  
else:  
    print("Invalid password")  # else print invalid