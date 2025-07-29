# steganography-tool
A python GUI tool to hide and extract and encrypt and decrypt messages inside image using LSB steganography
# Steganography Tool 🔐🖼️

A simple Python-based GUI application to hide and extract secret messages inside images using steganography.

## 📝 Features

- 🔏 Encode (hide) text messages inside image files.
- 🔍 Decode (extract) hidden messages from images.
- 🖼️ User-friendly GUI using Tkinter.
- 🐍 Uses `PIL` and `stepic` for steganography and image processing.

## 🚀 How to Use

### 🔐 Encrypt (Encode)
1. Open the application.
2. Select an image.
3. Type your secret message.
4. Click **Encode** to save the image with hidden data.

### 🔓 Decrypt (Decode)
1. Open the application.
2. Select the encoded image.
3. Click **Decode** to extract the hidden message.

## 🛠 Tools Used

- Python 3
- Tkinter
- Pillow (PIL)
- Stepic

## 🧰 How to Run

1. Install dependencies:
   ```bash
   pip install pillow stepic
