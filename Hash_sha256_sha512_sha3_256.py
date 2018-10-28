import hashlib

def sha_256():
	print("SHA-256")
	with open("File1KB.txt","rb") as obj_kb:
		kb = obj_kb.read()
		print(hashlib.sha_256(kb).hexdigest())

	with open("File1MB.txt","rb") as obj_mb:
		mb = obj_mb.read()
		print(hashlib.sha_256(mb).hexdigest())    

def sha_512():
	print("SHA-512")
	with open("File1KB.txt","rb") as obj_kb:
		kb = obj_kb.read()
		print(hashlib.sha_512(kb).hexdigest())

	with open("File1MB.txt","rb") as obj_mb:
		mb = obj_mb.read()
		print(hashlib.sha_512(mb).hexdigest())    
  

def sha3_256():
	print("SHA3-256")
	with open("File1KB.txt","rb") as obj_kb:
		kb = obj_kb.read()
		print(hashlib.sha3_256(kb).hexdigest())

	with open("File1MB.txt","rb") as obj_mb:
		mb = obj_mb.read()
		print(hashlib.sha3_256(mb).hexdigest())    
  
sha_256() 
sha_512()   	
sha3_256()
