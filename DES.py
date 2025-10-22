#!/usr/bin/env python3
from PIL import Image
from pathlib import Path
import matplotlib.pyplot as plt
import pyDes
import base64

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


def encrypt_bits_des(bit_string, key, width, height):
    # Convert bit string to bytes
    byte_data = int(bit_string, 2).to_bytes((len(bit_string) + 7) // 8, byteorder='big')
    # append width and height (4 bytes each) at the start
    dimensions = width.to_bytes(4, byteorder='big') + height.to_bytes(4, byteorder='big')
    byte_data_with_dims = dimensions + byte_data
    # Create DES cipher (ECB mode)
    des = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    # Encrypt
    encrypted_data = des.encrypt(byte_data_with_dims)
    
    return encrypted_data


def decrypt_bits_des(encrypted_data, key):
    # Create DES decipher
    des = pyDes.des(key, pyDes.ECB, padmode=pyDes.PAD_PKCS5)
    # Decrypt
    decrypted_data = des.decrypt(encrypted_data)
    # Extract width and height from the first 8 bytes
    width = int.from_bytes(decrypted_data[0:4], byteorder='big')
    height = int.from_bytes(decrypted_data[4:8], byteorder='big')
    # Get the actual image data
    image_bytes = decrypted_data[8:]
    # Convert bytes back to bit string
    bit_string = bin(int.from_bytes(image_bytes, byteorder='big'))[2:]
    
    return bit_string, width, height


if __name__ == "__main__":
    # DES key in bits (8 bytes = 64 bits)
    key = b"UNALENCR"

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
    encrypted_data = encrypt_bits_des(bit_string, key, width, height)
    
    # Use base 64 encoding to display encrypted data 
    encrypted_b64 = base64.b64encode(encrypted_data)
    print(f"Encrypted data (base64): {encrypted_b64}")

    # Decrypt process
    # Go from base 64 to bits again
    encrypted_data = base64.b64decode(encrypted_b64)
    # Decrypt the encrypted data (now extracts dimensions automatically)
    decrypted_bit_string, width, height = decrypt_bits_des(encrypted_data, key)
    reconstructed_img = bits_to_image(decrypted_bit_string, width, height)
    
    # Display the image using matplotlib
    plt.imshow(reconstructed_img)
    plt.axis('off')  # Hide axes
    plt.title('Reconstructed Image (After DES Encryption/Decryption)')
    plt.show()


