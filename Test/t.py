#SIRVE PARA AES https://onboardbase.com/blog/aes-encryption-decryption/#:~:text=AES%20requires%20a%20secret%20passphrase,256%2C%20or%20512%20bit%20long.
#pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
data = b'secret data'
header = b"header"
#key str
stringK = b'0123456789abcdef'#16
#Encryption
key = get_random_bytes(16)
print("key 1<>2",key,"<>",stringK)

cipher = AES.new(stringK, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
print("->",ciphertext)
nonce = cipher.nonce

#Decryption
cipher = AES.new(stringK, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)
print("-#",data)
print("-----------------------------------------")
