#!/usr/bin/env python3

# ROTATE LEFT
def encrypt(text, grilla):
	text = text.replace(" ", "")

	max_rotations = 4
	matrix_from_text_data = matrix_from_text(grilla)
	matrix_coordinates = create_matrix_from_coordinate_list(matrix_from_text_data)
	matrix_result = []
	for y in range(len(matrix_coordinates)):
		row = []
		for x in range(len(matrix_coordinates[0])):
			row.append("")
		matrix_result.append(row)

	textIdx = 0
	rot = 0
	while rot < max_rotations and textIdx < len(text):
		for x in range(len(matrix_coordinates)):
			for y in range(len(matrix_coordinates[x])):
				if matrix_coordinates[x][y] == True:
					matrix_result[x][y] = text[textIdx]
					textIdx += 1
					if textIdx >= len(text):
						break
		matrix_coordinates = rotate_matrix_left(matrix_coordinates)
		rot += 1

	return matrix_result


# ROTATE RIGHT
def decrypt(text, grilla):
	text = text.replace(" ", "")
	shift = shift
	result = ""
	return result


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


def create_matrix_from_coordinate_list(matrixKeyword):
	# Get list of coordinates, create matrix with largest coordinates
	# Then put true in those position, every other its false.
	max_x, max_y = find_matrix_size(matrixKeyword)
	matrix = []
	for y in range(max_y + 1):
		row = []
		for x in range(max_x + 1):
			row.append(False)
		matrix.append(row)

	# putting true values
	for coord in matrixKeyword:
		matrix[coord[0]][coord[1]] = True

	return matrix


def find_matrix_size(matrixKeyword):
	max_x = 0
	max_y = 0
	for coord in matrixKeyword:
		if coord[0] > max_x:
			max_x = coord[0]
		if coord[1] > max_y:
			max_y = coord[1]
	return [max_x, max_y]


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


def print_matrix(matrix):
	for row in matrix:
		for y in row:
			print(y, end="")
		print()


def main():
	grilla: str = input("Put grill as a list of coordinates ex. [[0,2],[2,0]]")
	elec: str = input("Put R to rotate right put L to rotate left").upper()

	if elec == "R":
		cipherTex = input("Put cipher text here: ").upper()
		print_matrix(decrypt(cipherTex, grilla))

	if elec == "L":
		plainTex = input("Put plain text here: ").upper()
		print_matrix(encrypt(plainTex, grilla))


if __name__ == "__main__":
	main()
