#!/usr/bin/env python3
import math

def EEA(a,b):
  if b == 0:
    return (a,1,0)

  q = math.floor(a/b)
  derivadaD,derivadaX,derivadaY = EEA(b,a % b)
  d,x,y = (derivadaD, derivadaY, derivadaX - q * derivadaY)
  #print("d: ",d , "x: ",x ,"y: ",y)
  return (d,x,y)

def encrypt(plainText : str, matrixKeyword : str, vocabulary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
  matrix = matrix_from_text(matrixKeyword)
  result = ""
  # Check plaintext par or size and fill
  left = len(plainText) % len(matrix)
  if left !=0 :
    for i in range(left):
      plainText += "X"
  
  matrixResult = []
  # loop of n pairs of size matrix.
  for i in range(0,len(plainText), len(matrix)):
    for j in range(0,len(matrix)):
      # t de i* len matrix + j
    # get t letters of size matrix (convert to int)
    
    pass
  # mult matrix and mod 26.
  # convert int to letter and append to result.
  return result


def matrix_from_text():
  pass

def main():
  elec : str = input("Put D to decrypt, E to encrypt (D|E)").upper()

  if elec == "D":
    cipherTex = input("Put cipher text here: ").upper()
    keyword = input("put matrix keyword here: ").upper()
    print(decrypt(cipherTex,keyword,t=t))

  if elec == "E":
    cipherTex = input("Put plain text here: ").upper()
    keyword = input("put keyword here: ").upper()
    print(encrypt(cipherTex,keyword,t=t))


if __name__ == "__main__":
    main()