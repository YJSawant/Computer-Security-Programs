from Crypto.Cipher import AES
from Crypto import Random
import time

#Random Key Generator
key = Random.new().read(AES.block_size)

#AES Encryption
start = time.clock()
for i in range(0,1000):
    cipher = AES.new(key, AES.MODE_ECB)
    message =cipher.encrypt(b'1234567891234567')

stop = time.clock()
print ("Cipher text is")
print (message)
print ("Time taken")
print (stop - start)

#Testing the using decrypt function
message1 =cipher.decrypt(message)
print ("Plain text after Decryption is")
print (message1)
