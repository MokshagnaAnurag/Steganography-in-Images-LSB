import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import numpy as np

def text_to_binary(text):
    """Convert text into binary representation with a special delimiter at the end."""
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string + '1111111111111110'  # Delimiter to mark end of message

def hide_text(image_path, secret_message, output_path):
    """Embed a secret message into an image using LSB steganography."""
    
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found!")
        return
    
    # Load and process the image
    img = Image.open(image_path).convert("RGB")  
    pixels = np.array(img)

    # Convert the message to binary
    binary_text = text_to_binary(secret_message)
    binary_index = 0
    max_capacity = pixels.size // 3  # Max bits that can be hidden

    # Ensure the message can fit inside the image
    if len(binary_text) > max_capacity:
        raise ValueError("Error: The message is too long for this image!")

    # Embed the message into the image
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # Iterate through R, G, B channels
                if binary_index < len(binary_text):
                    pixels[i, j, k] = (pixels[i, j, k] & 0xFE) | int(binary_text[binary_index])
                    binary_index += 1

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the encoded image
    encoded_img = Image.fromarray(pixels)
    encoded_img.save(output_path)
    
    print(f"Secret message successfully hidden in '{output_path}'")

def upload_and_encode():
    """Open a file dialog to let the user select an image and encode a secret message."""
    root = tk.Tk()
    root.withdraw()  # Hide the Tkinter main window

    # Open file dialog for image selection
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )
    
    if not file_path:
        print("No file selected. Exiting...")
        return

    # Prompt user to enter a secret message
    secret_message = input("Enter the secret message to hide: ")

    # Define the output path
    output_path = os.path.join("output", "encoded.png")
    
    # Hide the text inside the image
    hide_text(file_path, secret_message, output_path)

# Run the program
upload_and_encode()
