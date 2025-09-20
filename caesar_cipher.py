#!/usr/bin/env python3

def encrypt(text, shift, vocabulary : str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
  text = text.replace(" ","")
  shift = shift + 1
  result = ""
  for i in range(len(text)):
    oldChr = text[i]
    oldChrIdx = vocabulary.find(oldChr)
    newPos = (oldChrIdx + shift) % len(vocabulary)-1
    result += vocabulary[newPos]
  return result

def decrypt(text, shift, vocabulary : str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
  text = text.replace(" ","")
  shift = shift
  result = ""
  for i in range(len(text)):
    oldChr = text[i]
    oldChrIdx = vocabulary.find(oldChr)
    newPos = (oldChrIdx - shift)
    if newPos < 0:
      newPos = len(vocabulary)  + newPos
    else:
      newPos = newPos % (len(vocabulary) -1)
    result += vocabulary[newPos]
  return result

def main():
  elec : str = input("Put D to decrypt, E to encrypt (D|E)").upper()

  if elec == "D":
    cipherTex = input("Put cipher text here: ").upper()
    shift = int(input("put shift here: "))
    voc = input("put vocabulary here, left blank to use default: ").upper()
    if voc != "":
      print(decrypt(cipherTex,shift,voc))
    else:
      print(decrypt(cipherTex,shift))

  if elec == "E":
    plainTex = input("Put plain text here: ").upper()
    shift = int(input("put shift here: "))
    voc = input("put vocabulary here, left blank to use default: ").upper()
    if voc != "":
      print(encrypt(plainTex,shift,voc))
    else:
      print(encrypt(plainTex,shift))


if __name__ == "__main__":
    main()