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
  plainText = plainText.replace(" ","").upper()
  matrix = matrix_from_text(matrixKeyword)
  n = len(matrix)  # Get matrix size
  result = ""
  
  # Check if matrix is square
  if not all(len(row) == n for row in matrix):
    raise ValueError("Matrix must be square")
    
  # Check plaintext length and pad if needed
  if len(plainText) % n != 0:
    plainText += "X" * (n - (len(plainText) % n))
  
  matrixResult = []
  # Process text in blocks of size n
  for i in range(0, len(plainText), n):
    block = plainText[i:i+n]
    # Convert block to numbers
    blockNumbers = [vocabulary.index(char) for char in block]
    matrixResult.append(blockNumbers)
  
  matrixResultMultiplied = []
  # multiply matrix by matrixResult
  matrixResultMultiplied = matrix_multiplication(matrixResult, matrix)
  # mod
  for i in range(len(matrixResultMultiplied)):
    matrixResultMultiplied[i] = [x % len(vocabulary) for x in matrixResultMultiplied[i]]

  # convert int to letter and append to result.
  for row in matrixResultMultiplied:
    for num in row:
      result += vocabulary[num]
  return result

def decrypt(cipherText : str, matrixKeyword : str, vocabulary = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
  cipherText = cipherText.replace(" ","").upper()
  matrix = matrix_from_text(matrixKeyword)
  n = len(matrix)  # Get matrix size
  
  # Check if matrix is square
  if not all(len(row) == n for row in matrix):
    raise ValueError("Matrix must be square")
    
  inverse = find_modular_inverse(matrix, len(vocabulary))
  result = ""
  
  matrixResult = []
  # Process text in blocks of size n
  for i in range(0, len(cipherText), n):
    block = cipherText[i:i+n]
    # Convert block to numbers
    blockNumbers = [vocabulary.index(char) for char in block]
    matrixResult.append(blockNumbers)

  matrixResultMultiplied = []
  # multiply result by inverse
  matrixResultMultiplied = matrix_multiplication(matrixResult, inverse)
  # mod
  for i in range(len(matrixResultMultiplied)):
    matrixResultMultiplied[i] = [x % len(vocabulary) for x in matrixResultMultiplied[i]]
  # convert int to letter and append to result.
  for row in matrixResultMultiplied:
    for num in row:
      result += vocabulary[num]
  return result


def matrix_multiplication(A, B):
  # A is m x n
  # B is n x p
  # Result is m x p
  m = len(A)
  n = len(A[0])
  p = len(B[0])
  
  # Initialize result matrix with zeros
  result = [[0 for _ in range(p)] for _ in range(m)]
  
  for i in range(m):
    for j in range(p):
      for k in range(n):
        result[i][j] += A[i][k] * B[k][j]
  
  return result


def matrix_from_text(matrixKeyword : str) -> list:
  # This take a string and convert it to a matrix
  # The input is a list of lists
  # Example: "[[1,2],[3,4]]" ->  [[1,2],[3,4]]
  matrix = []
  current_row = []
  current_number = ""
  
  # Ignore first and last brackets
  for char in matrixKeyword[1:-1]:
    if char == "[":
      # Start a new row when we find opening bracket
      current_row = []
    elif char == "]":
      # When closing bracket found, add last number if exists
      if current_number:
        current_row.append(int(current_number))
        current_number = ""
      # Add completed row to matrix
      matrix.append(current_row)
    elif char.isdigit():
      # Build up multi-digit numbers
      current_number += char
    elif char == ",":
      # On comma, add the built-up number if exists
      if current_number:
        current_row.append(int(current_number))
        current_number = ""

  return matrix





def find_modular_inverse(matrix, mod):
  det = find_determinant(matrix)
  if det == 0:
    raise ValueError("Matrix is not invertible")
  # Find the modular inverse of matrix under modulo mod
  d, x, y = EEA(det, mod)
  if d != 1:
    raise ValueError("Modular inverse does not exist, this is not coprime")
  
  adjA = find_adjugate(matrix)

  inverse = x * adjA
  # Make modulate of inverse in base mod
  inverse = [[elem % mod for elem in row] for row in inverse]

  return inverse

def find_adjugate(matrix):
  # This function calculates the adjugate of a square matrix
  n = len(matrix)
  adj = [[0] * n for _ in range(n)]
  
  for i in range(n):
    for j in range(n):
      # Get minor matrix
      minor = [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]
      # Calculate cofactor
      cofactor = ((-1) ** (i + j)) * find_determinant(minor)
      adj[j][i] = cofactor  # Note the transpose here
  
  return adj


def find_determinant(matrix):
  # This function calculates the determinant of a square matrix
  n = len(matrix)
  if n == 1:
    return matrix[0][0]
  if n == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  
  det = 0
  for c in range(n):
    minor = [row[:c] + row[c+1:] for row in matrix[1:]]
    det += ((-1) ** c) * matrix[0][c] * find_determinant(minor)
  return det

def main():
  elec : str = input("Put D to decrypt, E to encrypt (D|E)").upper()

  if elec == "D":
    cipherTex = input("Put cipher text here: ").upper()
    keyword = input("put matrix keyword here: ").upper()
    print(decrypt(cipherTex,keyword))

  if elec == "E":
    cipherTex = input("Put plain text here: ").upper()
    keyword = input("put keyword here: ").upper()
    print(encrypt(cipherTex,keyword))


if __name__ == "__main__":
    main()