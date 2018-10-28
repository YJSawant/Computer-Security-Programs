<<<<<<< HEAD
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os,timeit

key = os.urandom(16)
def encrypt(ip, key):
		ip = pad(ip, AES.block_size)
		iv = os.urandom(16)
		
		encryptor = AES.new(key, AES.MODE_CBC, iv)
		start = timeit.default_timer()
		x=iv + encryptor.encrypt(ip)
		stop = timeit.default_timer()
		print('Time: ', stop - start)
		return x
def decrypt(ep, key):
		iv = ep[:AES.block_size]
		decryptor = AES.new(key, AES.MODE_CBC, iv)
		start = timeit.default_timer()
		y=decryptor.decrypt(ep[AES.block_size:])
		stop = timeit.default_timer()
		print('Time: ', stop - start)
		return unpad(y,AES.block_size)

def fileops1KB():
        testfile="File1KB.txt"
        with open(testfile,"rb") as infile:
            inputtext = infile.read()
            enctext = encrypt(inputtext, key)   
                
        with open("Enc1KB" + ".enc", 'wb') as outfile:
            outfile.write(enctext)    
        
        with open("Enc1KB.enc","rb") as infile:
            outputtext = infile.read()
            dectext = decrypt(outputtext, key)
	
        with open("Dec1KB" + ".txt", 'wb') as outfile:
            outfile.write(dectext)
        
def fileops1MB():
        testfile="File1MB.txt"
        with open(testfile,"rb") as infile:
            inputtext = infile.read()
            enctext = encrypt(inputtext, key)   
                
        with open("Enc1MB" + ".enc", 'wb') as outfile:
            outfile.write(enctext)    
        
        with open("Enc1MB.enc","rb") as infile:
            outputtext = infile.read()
            dectext = decrypt(outputtext, key)
	
        with open("Dec1MB" + ".txt", 'wb') as outfile:
            outfile.write(dectext)
        
fileops1KB()
fileops1MB()
        
=======
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os,timeit

key = os.urandom(16)
def encrypt(ip, key):
		ip = pad(ip, AES.block_size)
		iv = os.urandom(16)
		
		encryptor = AES.new(key, AES.MODE_CBC, iv)
		start = timeit.default_timer()
		x=iv + encryptor.encrypt(ip)
		stop = timeit.default_timer()
		print('Time: ', stop - start)
		return x
def decrypt(ep, key):
		iv = ep[:AES.block_size]
		decryptor = AES.new(key, AES.MODE_CBC, iv)
		start = timeit.default_timer()
		y=decryptor.decrypt(ep[AES.block_size:])
		stop = timeit.default_timer()
		print('Time: ', stop - start)
		return unpad(y,AES.block_size)

def fileops1KB():
        testfile="File1KB.txt"
        with open(testfile,"rb") as infile:
            inputtext = infile.read()
            enctext = encrypt(inputtext, key)   
                
        with open("Enc1KB" + ".enc", 'wb') as outfile:
            outfile.write(enctext)    
        
        with open("Enc1KB.enc","rb") as infile:
            outputtext = infile.read()
            dectext = decrypt(outputtext, key)
	
        with open("Dec1KB" + ".txt", 'wb') as outfile:
            outfile.write(dectext)
        
def fileops1MB():
        testfile="File1MB.txt"
        with open(testfile,"rb") as infile:
            inputtext = infile.read()
            enctext = encrypt(inputtext, key)   
                
        with open("Enc1MB" + ".enc", 'wb') as outfile:
            outfile.write(enctext)    
        
        with open("Enc1MB.enc","rb") as infile:
            outputtext = infile.read()
            dectext = decrypt(outputtext, key)
	
        with open("Dec1MB" + ".txt", 'wb') as outfile:
            outfile.write(dectext)
        
fileops1KB()
fileops1MB()
        
>>>>>>> 7dbc8b55fb7531ce23df14ddc31145b7117616c6
