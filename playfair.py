#!/usr/bin/env python3
# Playfair taller

def encrypt(text,keyMatrix):
    # Manipulate text to fit the Playfair cipher rules
    cleanText = clean_text(text)
    # Encryption
    encryptedText = ""
    for i in range(len(cleanText)):
        pair = cleanText[i]
        row1, col1 = find_position(pair[0], keyMatrix)
        row2, col2 = find_position(pair[1], keyMatrix)
        if row1 == row2:
            # Same row: shift right
            encryptedText += keyMatrix[row1][(col1 + 1) % 5]
            encryptedText += keyMatrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            # Same column: shift down
            encryptedText += keyMatrix[(row1 + 1) % 5][col1]
            encryptedText += keyMatrix[(row2 + 1) % 5][col2]
        else:
            # Rectangle: swap columns
            encryptedText += keyMatrix[row1][col2]
            encryptedText += keyMatrix[row2][col1]

    return encryptedText


def decrypt(text,keyMatrix):
    # Manipulate text to fit the Playfair cipher rules
    cleanText = clean_text(text)
    # Desencryption
    decryptedText = ""
    for i in range(len(cleanText)):
        pair = cleanText[i]
        row1, col1 = find_position(pair[0], keyMatrix)
        row2, col2 = find_position(pair[1], keyMatrix)
        if row1 == row2:
            # Same row: shift left
            decryptedText += keyMatrix[row1][(col1 - 1) % 5]
            decryptedText += keyMatrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # Same column: shift up
            decryptedText += keyMatrix[(row1 - 1) % 5][col1]
            decryptedText += keyMatrix[(row2 - 1) % 5][col2]
        else:
            # Rectangle: swap columns
            decryptedText += keyMatrix[row1][col2]
            decryptedText += keyMatrix[row2][col1]

    return decryptedText


def find_position(char, keyMatrix):
    for i in range(5):
        for j in range(5):
            if keyMatrix[i][j] == char:
                return i, j
    return None


def clean_text(text):
    array_text = []
    for i in range(len(text)):
        if text[i] == "I" or text[i] == "J":
            array_text.append("IJ")
        else:
            array_text.append(text[i])
    pair_text = []
    i = 0
    while i < len(array_text):
        pair = []
        # Handle same letter in a pair or odd length
        if i < len(array_text) - 1 and array_text[i] == array_text[i+1]:
            pair.append(array_text[i])
            pair.append('X')
            i += 1
        # Handles normal pairs
        elif i < len(array_text):
            pair.append(array_text[i])
            if i + 1 >= len(array_text):
                pair.append('X')
            else:
                pair.append(array_text[i+1])
            i += 2
        pair_text.append(pair)
    return pair_text


def generate_matrix_from_key(key):
    array_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'IJ', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    array_key = []
    key = "".join(dict.fromkeys(key))  # Remove duplicates while preserving order
    for char in key:
        if char == "I" or char == "J":
            if "IJ" not in array_key:
                array_key.append("IJ")
                array_alphabet.remove("IJ")
        elif char not in array_key and char in array_alphabet:
            array_key.append(char)
            array_alphabet.remove(char)

    if len(array_key) < 25:
        array_key.extend(array_alphabet)

    keyMatrix = []
    for i in range(5):
        row = array_key[i*5:(i+1)*5]
        keyMatrix.append(row)

    return keyMatrix


def main():
    key = input("Enter the keyword (key) maximum of 20 characters: ")[:20].upper()
    clearText = input("Enter the text to encrypt or decrypt: ").upper().replace(" ", "")
    choice = input("To Encrypt put E to decrypt put D: ").strip().upper()

    keyMatrix = generate_matrix_from_key(key)
    print("Key Matrix:" , keyMatrix)

    if choice == 'E':
        encryptedText = encrypt(clearText, keyMatrix)
        print("Encrypted Text:", encryptedText)
    elif choice == 'D':
        decryptedText = decrypt(clearText, keyMatrix)
        print("Decrypted Text:", decryptedText)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()