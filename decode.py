import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import numpy as np

def binary_to_text(binary_string):
    """Convert binary data to human-readable text, stopping at the delimiter."""
    characters = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    message = ""

    for char in characters:
        if char == "1111111111111110":  # Stop at the delimiter
            break
        message += chr(int(char, 2))  # Convert binary to text

    return message

def extract_text(image_path):
    """Extract hidden text from an image using LSB steganography."""
    if not os.path.exists(image_path):
        messagebox.showerror("Error", f"Image file '{image_path}' not found!")
        return
    
    img = Image.open(image_path).convert("RGB")
    pixels = np.array(img)
    
    binary_text = ""

    # Extract LSB from RGB values
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):
                binary_text += str(pixels[i, j, k] & 1)  # Extract the last bit

    # Convert binary data to readable text
    secret_message = binary_to_text(binary_text)
    
    if secret_message:
        messagebox.showinfo("Extracted Message", f"🔍 Secret Message: {secret_message}")
    else:
        messagebox.showwarning("No Hidden Message", "No secret message found in this image!")

    return secret_message

def open_file():
    """Open file dialog to select an image for decoding."""
    file_path = filedialog.askopenfilename(
        title="Select an Image to Extract Message",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )

    if file_path:
        extract_text(file_path)

# Create GUI Window
root = tk.Tk()
root.title("🔍 Image Steganography - Extract Text")

# Window size
root.geometry("400x250")

# Heading Label
tk.Label(root, text="Image Steganography - Extract Hidden Text", font=("Arial", 14, "bold"), pady=10).pack()

# Select Image Button
extract_button = tk.Button(root, text="Select Image", command=open_file, font=("Arial", 12), padx=20, pady=10)
extract_button.pack(pady=20)

# Run the Tkinter GUI
root.mainloop()
