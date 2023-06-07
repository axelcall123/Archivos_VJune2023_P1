#SIRVE PARA AES https://onboardbase.com/blog/aes-encryption-decryption/#:~:text=AES%20requires%20a%20secret%20passphrase,256%2C%20or%20512%20bit%20long.
#pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from Crypto.Util.Padding import pad, unpad

import json


data = b'secret data'
header = b"header"
#key str
stringK = b'miaproyecto12345'  # 16
#Encryption
# Key for encryption and decryption (must be 16, 24, or 32 bytes long)
# key = get_random_bytes(16)
# print("key 1<>2",key,"<>",stringK)

cipher = AES.new(stringK, AES.MODE_EAX)#se cambia los modos AES.MODE_EAX
ciphertext, tag = cipher.encrypt_and_digest(data)
print("->", ciphertext.hex())
nonce = cipher.nonce

#Decryption
cipher = AES.new(stringK, AES.MODE_EAX, nonce)#se cambia los modos AES.MODE_EAX
data = cipher.decrypt_and_verify(ciphertext, tag)
print("-#",data)
print("1---------------------")

#https://bobbyhadz.com/blog/python-unicodedecodeerror-ascii-codec-cant-decode-byte
my_text = '𝘈Ḇ𝖢𝕯٤ḞԍНǏ'
my_binary_data = my_text.encode('utf-8')
# 👇️ set errors to ignore
my_text_again = my_binary_data.decode('utf-8', errors='ignore')
print(my_text_again)
print("2---------------------")
#https://sparkbyexamples.com/python/python-convert-bytes-to-string/
byte_string = b'\xff\xfes\x00p\x00a\x00r\x00k\x00b\x00y\x00e\x00x\x00a\x00m\x00p\x00l\x00e\x00s\x00'
string = byte_string.decode('utf-16')
print(string)
print("3---------------------")
# AES ECB encryption

def encrypt_string(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

# AES ECB decryption
def decrypt_string(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data.decode('utf-8')
# String to encrypt
plaintext = "Hello, World!"
# Encrypting the string
encrypted_data = encrypt_string(stringK, plaintext)
# Decrypting the string
decrypted_data = decrypt_string(stringK, encrypted_data)
# Printing the results
print("Original String:", plaintext)
print("Encrypted Data:", encrypted_data.hex())
print("Decrypted String:", decrypted_data)
