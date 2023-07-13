from cryptography.fernet import Fernet

message = input("Enter your plaintext: ")

key = Fernet.generate_key()
Fernet = Fernet(key)

ciphertext = Fernet.encrypt(message.encode())

#print("Orignal Message: ", message)
print("Encrypted Message: ", ciphertext)

dcrypt = Fernet.decrypt(ciphertext).decode()

print("Decrypted Message: ", dcrypt)

