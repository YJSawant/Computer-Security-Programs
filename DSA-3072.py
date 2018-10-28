from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

def signing_verify(testfile):
    privatekey = dsa.generate_private_key( key_size=3072, backend=default_backend())
	
	with open(testfile,"rb") as inputfile:
            inputdata = inputfile.read()

	sign = privatekey.sign( inputdata,hashes.SHA256())
	print("DSA Signature for 1 KB file:\n ",sig,"\n")

	publickey = privatekey.public_key()
	pubblickey.verify( sign, inputdata, hashes.SHA256())

def file1KB():
        testfile="File1KB.txt"
        signing_verify(testfile)

def file1MB():
        testfile="File1MB.txt"
        signing_verify(testfile)

file1KB()
file1MB()
