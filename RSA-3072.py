# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 21:23:21 2018

@author: DELL
"""

from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.PublicKey import RSA

encryptkey = RSA.generate(3072)
privatekey = encryptkey.export_key()
with open("private.pem","wb") as private:
	private.write(privatekey)

publickey = encryptkey.publickey().export_key()	 
with open("public.pem","wb") as public:
        public.write(publickey)

def encrypt(testfile,encfile):
    	
	CHUNK_SIZE = 16
	encrypteddata = b''
	with open(testfile,"rb") as inputfile:
                chunk = inputfile.read(CHUNK_SIZE)
		while chunk:
                    publickey = RSA.importKey(open("public.pem").read())
                    paddedpub = PKCS1_OAEP.new(publickey)
                    encrypteddata += paddedpub.encrypt(chunk)
                    chunk = inputfile.read(CHUNK_SIZE)

                inputfile.close()

	with open(encfile,'wb') as outputfile:
		outputfile.write(encrypteddata)

def decrypt(encfile,decfile):
    
	CHUNK_SIZE = 384
	msg = b''
	with open(encfile,"rb") as inputfile:
		chunk = inputfile.read(CHUNK_SIZE)
		while chunk:
			privatekey = RSA.importKey(open('private.pem').read())
			paddedpriv = PKCS1_OAEP.new(privatekey)
			msg += paddedpriv.decrypt(chunk)
			chunk = inputfile.read(CHUNK_SIZE) 
		inputfile.close()


	with open(testfile,'wb') as outputfile:
		outputfile.write(msg)

def file1KB():
        testfile="File1KB.txt"
        encfile="Enc1KB.enc"
        encrypt(testfile,encfile)
        decfile="Dec1KB.txt"
        decrypt(encfile,decfile)
        
def file1MB():
        testfile="File1MB.txt"
        encfile="Enc1MB.enc"
        encrypt(testfile,encfile)
        decfile="Dec1MB.txt"
        decrypt(encfile,decfile)
        
file1KB()
file1MB()
