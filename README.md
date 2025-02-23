# Steganography-LSB

This project implements image steganography using the Least Significant Bit (LSB) method.

## 📂 Project Structure
```
📂 Steganography-LSB
│-- 📂 images/              # Store input/output images
│-- 📂 output/              # Store images with hidden text
│-- encode.py               # Script to hide text in an image
│-- decode.py               # Script to extract hidden text
│-- requirements.txt        # Dependencies
│-- README.md               # Project description
```

## 🚀 Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Hide text inside an image:
   ```bash
   python encode.py
   ```

3. Extract hidden text from an image:
   ```bash
   python decode.py
   ```

## 🛠 How It Works

- The `encode.py` script hides text inside an image by modifying the least significant bits of pixel values.
- The `decode.py` script extracts the hidden message from the image.

Enjoy encoding and decoding secret messages! 🔐
