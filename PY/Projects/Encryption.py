from cryptography.fernet import Fernet

plaintext = input ("enter string to encrypt: ")

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(plaintext.encode())


print("Plaintext: " + plaintext)
print("Ciphertext: " + encMessage)


