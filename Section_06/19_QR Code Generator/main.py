# Import the qrcode library and alias it as pyqr for easier usage
import qrcode as pyqr

def Qrcode_maker(data):
    """
    Creates a QR code image from the provided data.
    
    Args:
        data (str): The data to encode in the QR code (e.g., URL, text)
    
    Returns:
        None: Saves the QR code image to a file named 'qr_code.png'
    """
    # Initialize QR code object with specific parameters
    qr = pyqr.QRCode(
        version=1,      # Version 1 supports up to 41x41 modules
        border=5,       # Add a 5-module border around the QR code
        box_size=10,    # Size of each module (pixel) in the QR code
    )
    
    # Add the data to the QR code
    qr.add_data(data)

    # Generate the QR code and automatically determine optimal size
    qr.make(fit=True)

    # Create the QR code image with specified colors
    pic = qr.make_image(fill_color="black", back_color="white")
    # Save the generated QR code as a PNG file
    pic.save("qr_code.png")

    # Print success message
    print("QR code generated and saved as qr_code.png successfully.")

# Example usage: Generate QR code for a YouTube channel
Qrcode_maker('https://www.youtube.com/@ainertia/shorts')