import os

from crypto import derive_key, encrypt, decrypt



password = input("Master password: ")

salt = os.urandom(16)

key = derive_key(password, salt)

message = b"Hello world but encrypted"

nonce, ciphertext = encrypt(message, key)

print("Ciphertext:", ciphertext.hex())

plaintext = decrypt(ciphertext, key, nonce)

print ("Decrypted:", plaintext.decode())