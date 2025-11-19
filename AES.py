#!/usr/bin/env python3
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import pyaes
import base64
import os

def image_to_bits(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert image to RGB if it has an alpha channel
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Get image dimensions
    width, height = img.size
    # Get pixel data as a flat list of bytes
    pixel_data = list(img.getdata())
    # Flatten the pixel tuples
    flat_bytes = []
    for pixel in pixel_data:
        for value in pixel:
            flat_bytes.append(value)
    
    # Convert each byte to 8-bit binary representation
    bit_string = ''.join(format(byte, '08b') for byte in flat_bytes)
    
    
    # Store metadata for reconstruction
    image_data = {
        'width': width,
        'height': height,
        'mode': 'RGB'
    }
    print("image data: ",image_data)
    return bit_string, image_data


def bits_to_image(bit_string, width, height):
    # Convert bit string to bytes
    byte_array = []
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        byte_array.append(int(byte, 2))
    
    # Convert bytes back to pixel tuples (RGB)
    pixels = []
    for i in range(0, len(byte_array), 3):
        pixel = tuple(byte_array[i:i+3])
        pixels.append(pixel)

    # Create new image from pixel data
    img = Image.new('RGB', (width, height))
    img.putdata(pixels)
    
    return img


def encrypt_bits_aes(bit_string, key, width, height, sec_level, iv):
    # Convert bit string to bytes
    byte_data = int(bit_string, 2).to_bytes((len(bit_string) + 7) // 8, byteorder='big')
    # append width and height (4 bytes each) at the start
    dimensions = width.to_bytes(4, byteorder='big') + height.to_bytes(4, byteorder='big')
    byte_data_with_dims = dimensions + byte_data
    #print(byte_data_with_dims)
    # Create AES cipher
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(byte_data_with_dims)
    #print("AES W H", byte_data_with_dims[:8])
    return encrypted_data


def decrypt_bits_aes(encrypted_data, key):
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)
    #print("DEC DATA 8", decrypted_data[:8])
    # Extract width and height from the first 8 bytes
    width = int.from_bytes(decrypted_data[0:4], byteorder='big')
    height = int.from_bytes(decrypted_data[4:8], byteorder='big')
    # Get the actual image data
    image_bytes = decrypted_data[8:]
    # Convert bytes back to bit string
    bit_string = bin(int.from_bytes(image_bytes, byteorder='big'))[2:]
    print(width, " ",height)
    return bit_string, width, height


if __name__ == "__main__":
    # keys
    key_128 = os.urandom(16)
    key_192 = os.urandom(24)
    key_256 = os.urandom(32)
    # For some modes of operation we need a random initialization vector
    # of 16 bytes
    iv = os.urandom(16)

    # Security level 128,192,256 from input
    sec_level = int(input("Select level of security \n(1: 128 bits, 2: 192 bits, 3: 256 bits)"))
    
    if sec_level == 1:
        key = key_128
    if sec_level == 2:
        key = key_192
    if sec_level == 3:
        key = key_256
    

    # Get path to current directory
    current_directory = Path(__file__).parent.absolute()
    image_path = input("Put image name, must be in file directory: ")
    # Open image
    test = Image.open(current_directory/image_path)
    print(f"Reading image from: {current_directory/image_path}")
    
    bit_string, image_data = image_to_bits(current_directory/image_path)
    
    width = image_data['width']
    height = image_data['height']
    
    # Encrypt the bit string
    encrypted_data = encrypt_bits_aes(bit_string, key, width, height, sec_level, iv)
    
    # Use base 64 encoding to display encrypted data 
    encrypted_b64 = base64.b64encode(encrypted_data)
    print(f"Encrypted data (base64): {encrypted_b64}")

    # Decrypt process
    # Go from base 64 to bits again
    encrypted_data = base64.b64decode(encrypted_b64)
    # Decrypt the encrypted data (now extracts dimensions automatically)
    decrypted_bit_string, width, height = decrypt_bits_aes(encrypted_data, key)
    reconstructed_img = bits_to_image(decrypted_bit_string, width, height)
    
    # Display the image using matplotlib
    plt.imshow(reconstructed_img)
    plt.axis('off')  # Hide axes
    plt.title('Reconstructed Image (After DES Encryption/Decryption)')
    plt.show()


