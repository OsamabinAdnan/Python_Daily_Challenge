# Create a QR Code Generator!

# Import required libraries
import qrcode  # Main QR code generation library
import qrcode.constants  # Constants for QR code configuration

def generate_qr_code(data, filename = 'qr_code.png'):
    """
    Generate a QR code from the given data and save it to a file.
    Parameters:
        data (str): The text or URL to encode in the QR code.
        filename (str): The name of the output image file (defaults to 'qr_code.png').
    """
    # Create QR code instance with specific configuration
    qr = qrcode.QRCode(
        version=1,  # QR code version (1 to 40, controls the size of the QR code)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Level of error correction (L = 7% recovery) (M = 15% recovery) (Q = 25% recovery) (H = 30% recovery)
        box_size=10,  # Size of each box in pixels
        border=4,  # Border size in boxes
    )

    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)  # Fit ensures the QR code size is appropriate for the data

    # Create the QR code image with specified colors
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image to a file
    img.save(filename)
    print(f"QR code saved as {filename}")

    # Open the QR code image with the default image viewer
    img.show()


# Get user input for QR code content
text_to_url = input("Enter text to encode in QR code: ")

# Call the function to generate and save QR code
generate_qr_code(text_to_url)
