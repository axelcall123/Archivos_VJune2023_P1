#SIRVE PARA AES 
#pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
data = b'secret data'
header = b"header"
#Encryption
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
print("->",ciphertext)
nonce = cipher.nonce
#Decryption
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print("-#",data)