#!/usr/bin/env python3

# ROTATE LEFT
def encrypt(text, grilla, matrix_size, rotation_direction):
	text = text.replace(" ", "")
	max_rotations = 4
	matrix_from_text_data = matrix_from_text(grilla)
	matrix_coordinates : list[list[bool]] = create_matrix_from_coordinate_list(matrix_from_text_data, matrix_size)
	matrix_result = []
	for y in range(len(matrix_coordinates)):
		row = []
		for x in range(len(matrix_coordinates[0])):
			row.append("")
		matrix_result.append(row)
	textIdx = 0
	rot = 0
	while rot < max_rotations and textIdx < len(text)-1:
		for x in range(len(matrix_coordinates)):
			for y in range(len(matrix_coordinates[x])):
				if matrix_coordinates[x][y] == True:
					matrix_result[x][y] = text[textIdx]
					textIdx += 1
					if textIdx >= len(text):
						break
		if rotation_direction == "L":
			matrix_coordinates = rotate_matrix_left(matrix_coordinates)
		else:
			matrix_coordinates = rotate_matrix_right(matrix_coordinates)
		rot += 1
	return matrix_result


def decrypt(cipher_text, grilla, matrix_size, rotation_direction):
	# Step 1: Fill the matrix with cipher text (row by row)
	cipher_matrix = text_to_matrix(cipher_text, matrix_size)
	# Step 2: Prepare grille coordinates
	matrix_from_text_data = matrix_from_text(grilla)
	matrix_coordinates : list[list[bool]] = create_matrix_from_coordinate_list(matrix_from_text_data, matrix_size)
	# Step 3: Extract characters using grille rotations (same sequence as encryption)
	decrypted_message = ""
	max_rotations = 4
	for rot in range(max_rotations):
		# Read characters visible through grille holes
		for x in range(len(matrix_coordinates)):
			for y in range(len(matrix_coordinates[x])):
				if matrix_coordinates[x][y] == True:
					if x < len(cipher_matrix) and y < len(cipher_matrix[x]):
						decrypted_message += cipher_matrix[x][y]
		if rotation_direction == "L":
			matrix_coordinates = rotate_matrix_left(matrix_coordinates)
		else:
			matrix_coordinates = rotate_matrix_right(matrix_coordinates)
	return decrypted_message


def rotate_matrix_right(matrix):
	n = len(matrix)
	m = len(matrix[0])
	# Transpose the matrix
	transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(m)]
	# Reverse each row
	rotated_matrix = [[row[i] for i in range(m - 1, -1, -1)] for row in transposed_matrix]
	return rotated_matrix


# Auxiliars function to rotate matrix
# An Inplace function to rotate
# N x N matrix by 90 degrees in
# anti-clockwise direction
def rotate_matrix_left(mat):
	N = len(mat)
	# Consider all squares one by one
	for x in range(0, int(N / 2)):
		# Consider elements in group of 4 in current square
		for y in range(x, N - x - 1):
			# store current cell in temp variable
			temp = mat[x][y]
			# move values from right to top
			mat[x][y] = mat[y][N - 1 - x]
			# move values from bottom to right
			mat[y][N - 1 - x] = mat[N - 1 - x][N - 1 - y]
			# move values from left to bottom
			mat[N - 1 - x][N - 1 - y] = mat[N - 1 - y][x]
			# assign temp to left
			mat[N - 1 - y][x] = temp
	return mat


def create_matrix_from_coordinate_list(matrixKeyword, matrix_size):
	# Get list of coordinates, create matrix with given size
	# Then put true in those position, every other its false.
	matrix = []
	for y in range(matrix_size):
		row = []
		for x in range(matrix_size):
			row.append(False)
		matrix.append(row)
	# putting true values
	for coord in matrixKeyword:
		matrix[coord[0]][coord[1]] = True
	return matrix


def matrix_from_text(matrixKeyword: str) -> list:
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


def text_to_matrix(text, matrix_size):
	text = text.replace(" ", "")
	matrix = []
	char_idx = 0
	for i in range(matrix_size):
		row = []
		for j in range(matrix_size):
			if char_idx < len(text):
				row.append(text[char_idx])
				char_idx += 1
			else:
				row.append("")
		matrix.append(row)
	return matrix

def print_matrix(matrix):
	for row in matrix:
		for y in row:
			print(y, end="")
		print()


def main():
	matrix_size = int(input("Enter the size (n) of the square matrix (n x n): "))
	mode = input("Enter E for encryption or D for decryption: ").upper()
	elec: str = input("Put R to rotate right put L to rotate left: ").upper()
	grilla: str = input("Put grill as a list of coordinates ex. [[0,2],[2,0]]: ")
	
	if mode == "D":
		cipherTex = input("Put cipher text here: ").upper()
		if elec == "R":
			decrypted_text = decrypt(cipherTex, grilla, matrix_size, "R")
			print("Decrypted message:", decrypted_text)
		if elec == "L":
			decrypted_text = decrypt(cipherTex, grilla, matrix_size, "L")
			print("Decrypted message:", decrypted_text)

	if mode == "E":
		plainTex = input("Put plain text here: ").upper()
		if elec == "R":
			print("Encrypted matrix:")
			print_matrix(encrypt(plainTex, grilla, matrix_size, "R"))
		if elec == "L":
			print("Encrypted matrix:")
			print_matrix(encrypt(plainTex, grilla, matrix_size, "L"))


if __name__ == "__main__":
	main()


# Example Grille
# [[0,0],[2,1],[2,3],[3,2]]    

# Example grille 2
# [
# [0,0],[0,3],[0,5],
# [1,2],[1,8],
# [2,1],[2,6],
# [3,2],[3,4],[3,7],
# [4,4],[4,6],[4,8],
# [5,3],[5,7],
# [6,0],[6,5],
# [7,1],[7,4],[7,8],
# [8,2]
# ]