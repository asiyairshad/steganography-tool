from PIL import Image
from cryptography.fernet import Fernet
import base64
import hashlib

# Function to create encryption key from password
def generate_key(password):
    return base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())

def encrypt_message(message, password):
    key = generate_key(password)
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()

def decrypt_message(encrypted_message, password):
    key = generate_key(password)
    f = Fernet(key)
    try:
        decrypted = f.decrypt(encrypted_message.encode())
        return decrypted.decode()
    except:
        return "[Error: Wrong password or corrupted data]"

def encode_message(image_path, message, password, output_path):
    encrypted_message = encrypt_message(message, password)
    binary_message = ''.join([format(ord(i), '08b') for i in encrypted_message]) + '1111111111111110'

    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    for row in range(height):
        for col in range(width):
            if index < len(binary_message):
                pixel = list(img.getpixel((col, row)))
                for i in range(3):
                    if index < len(binary_message):
                        pixel[i] = pixel[i] & ~1 | int(binary_message[index])
                        index += 1
                encoded.putpixel((col, row), tuple(pixel))

    encoded.save(output_path)

def decode_message(image_path, password):
    img = Image.open(image_path)
    binary_message = ""
    for row in range(img.height):
        for col in range(img.width):
            pixel = img.getpixel((col, row))
            for color in pixel[:3]:
                binary_message += str(color & 1)

    all_bytes = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    encrypted_message = ""
    for byte in all_bytes:
        if byte == '11111110':  # EOF
            break
        encrypted_message += chr(int(byte, 2))

    return decrypt_message(encrypted_message, password)
