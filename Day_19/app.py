# Import required libraries
from PIL import Image  # PIL (Python Imaging Library) for image processing
import os  # For file and path operations

# Define ASCII characters array where:
# @ represents the darkest pixels
# Space represents the lightest pixels
# Characters in between represent varying levels of gray
ASCII_CHARS = "@#*+=-. "  # Ordered from darkest to lightest

def image_to_ascii(image_path, new_width=100):
    """
    Converts an image to ASCII art.
    :param image_path: Path to the image file
    :param new_width: Width of ASCII output (adjust as needed)
    :return: String containing the ASCII art
    """
    # Validate if the image file exists before processing
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found.")
        return ""
    
    # Open the image using PIL library
    image = Image.open(image_path)
    
    # Convert image to grayscale (L mode = single channel grayscale, 0-255)
    image = image.convert("L")
    
    # Calculate new dimensions while preserving aspect ratio
    width, height = image.size
    aspect_ratio = height / width
    # Multiply by 0.5 because terminal characters are taller than they are wide
    new_height = int(aspect_ratio * new_width * 0.5)
    # Resize image to new dimensions
    image = image.resize((new_width, new_height))
    
    # Get pixel data from image
    pixels = image.getdata()
    # Convert each pixel to an ASCII character
    # Divide by 36 to map 256 grayscale values to 7 ASCII characters
    ascii_str = "".join(ASCII_CHARS[pixel // 36] for pixel in pixels)
    
    # Split the long string into lines based on the new width
    # This creates proper line breaks for the ASCII art
    ascii_image = "\n".join([ascii_str[i:i+new_width] for i in range(0, len(ascii_str), new_width)])
    
    return ascii_image

# Specify the path to your input image
# Note: Update this path to point to your actual image file
image_path = r"G:\osamabinadnan_files\giaic\quarter_03\Python\Python_Daily_Challenge\Day_19\your_image.jpg"

# Convert image to ASCII and store the result
ascii_art = image_to_ascii(image_path)

# If conversion was successful (ascii_art is not empty)
if ascii_art:
    # Display the ASCII art in the console
    print(ascii_art)

    # Save the ASCII art to a text file named 'ascii_art.txt'
    with open("ascii_art.txt", "w") as f:
        f.write(ascii_art)