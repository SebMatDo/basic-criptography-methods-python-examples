#!/usr/bin/env python3
import hashlib

def md5(txt):
    md5 = hashlib.md5()
    md5.update(txt)
    return md5.hexdigest()

def sha1(txt):
    sha = hashlib.sha1()
    sha.update(txt)
    return sha.hexdigest()

def sha3(txt):
	sha3 = hashlib.sha3_512()
	sha3.update(txt)
	return sha3.hexdigest()

# Example Usage:
if __name__ == "__main__":
    # Find k such that 2^k = 3 (mod 5)
    print("Devuelve el hash en md5 y sha-1")
    txt = input("Escribe aqui el string: ")
    salt = input("Escribe aqui la sal: ")
    conc = txt+salt
    byteconc = bytes(conc,"utf-8")
    print("MD5: ",md5(byteconc))
    print("SHA-1: ",sha1(byteconc))
    print("SHA-3: ",sha3(byteconc))
    
    