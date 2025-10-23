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

  # Multiply each element of the adjugate by the determinant inverse
  inverse = [[elem * x for elem in row] for row in adjA]
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
  matrix_str = input("Put matrix as array: ")
  mod = int(input("Put mod here as int: "))
  matrix = matrix_from_text(matrix_str)
  inverse = find_modular_inverse(matrix,mod)
  print("inverse is: ", inverse)


if __name__ == "__main__":
    main()