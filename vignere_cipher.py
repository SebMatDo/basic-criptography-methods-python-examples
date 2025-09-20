#!/usr/bin/env python3

#Create matrix
# A-Z per row, then shift it 1 to the right each ocnsecuent row.
def create_vignere_matrix(abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
  matrix = []
  total_row = len(abc)
  total_col = len(abc)
  for i in range(total_row):
    row = []
    for j in range(total_col):
      idx = (j+i) % len(abc)
      row.append(abc[idx])
    matrix.append(row)
  return matrix

def encrypt(plainText, keyword, abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", t=5):
  # To encrypt we check two pair characters, the one of plain text is row
  # The one in keyword is col.
  # The cipher text would be the intersection of each pair in the matrix
  matrix = create_vignere_matrix(abc)
  idxKeyword = 0 # This one should cycle as long as we need it use module.
  idxPlainText = 0
  cipherText = ""
  plainText = plainText.replace(" ","")
  keyword = keyword.replace(" ","")
  while idxPlainText < len(plainText):
    chrRowIdx = abc.find(plainText[idxPlainText])
    chrColIdx = abc.find(keyword[idxKeyword])
    chrMatrix = matrix[chrRowIdx][chrColIdx]
    #print(chrRowIdx, " ", chrColIdx)
    # Append chr matrix to cipher text
    if idxPlainText%t == 0:
      cipherText += " "
    cipherText += chrMatrix
    idxKeyword += 1
    idxKeyword = idxKeyword % len(keyword)
    idxPlainText += 1

  return cipherText


def decrypt(cipherText : str, keyword, abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", t=5):
  # To decrypt we check two pair characters, the one of cipher text is intersection
  # The one in keyword is col.
  # Plain text would be search the row of intersection of key and cipher.
  matrix = create_vignere_matrix(abc)
  idxKeyword = 0 # This one should cycle as long as we need it use module.
  idxCipherText = 0
  plainText = ""
  cipherText = cipherText.replace(" ","")
  keyword = keyword.replace(" ","")
  while idxCipherText < len(cipherText):
    chrColIdx = abc.find(keyword[idxKeyword])
    chrMatrix = cipherText[idxCipherText]
    chrRowIdx = get_row_from_intersection(chrColIdx, chrMatrix, matrix) # Need to find this
    # Append chr matrix to cipher text
    if idxCipherText%t == 0:
      plainText += " "
    plainText += abc[chrRowIdx]
    idxKeyword += 1
    idxKeyword = idxKeyword % len(keyword)
    idxCipherText += 1

  return plainText

def get_row_from_intersection(chrColIdx, chrMatrix, matrix):
  # Search the char in the col, return the row.
  for i in range(len(matrix[chrColIdx])):
    if matrix[i][chrColIdx] == chrMatrix:
      return i
  return -1

def main():
  elec : str = input("Put D to decrypt, E to encrypt (D|E)").upper()

  if elec == "D":
    cipherTex = input("Put cipher text here: ").upper()
    keyword = input("put keyword here: ").upper()
    t = int(input("put t value here: "))
    print(decrypt(cipherTex,keyword,t=t))

  if elec == "E":
    cipherTex = input("Put plain text here: ").upper()
    keyword = input("put keyword here: ").upper()
    t = int(input("put t value here: "))
    print(encrypt(cipherTex,keyword,t=t))


if __name__ == "__main__":
    main()