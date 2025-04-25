# QR Code Generator

A simple Python script that generates QR codes from any text or URL input.

## Features

- Generates high-quality QR codes
- Customizable QR code parameters (version, border, size)
- Black and white QR code output
- Saves output as PNG file

## Dependencies

- Python 3.x
- `qrcode` library

## Installation

1. Make sure you have Python installed on your system
2. Install the required library:
   ```
   pip install qrcode
   ```

## Usage

1. Import the script:
   ```python
   import qrcode as pyqr
   ```

2. Call the `Qrcode_maker` function with your data:
   ```python
   Qrcode_maker('https://your-url-here.com')
   ```

3. The QR code will be saved as 'qr_code.png' in the current directory.

## Example Output

Below is an example of a generated QR code:

![QR Code Example](qr_code.png)

## Parameters

The QR code generator uses the following parameters:
- `version`: 1 (supports up to 41x41 modules)
- `border`: 5 modules
- `box_size`: 10 pixels per module

## License

This project is open source and available for personal and commercial use.

## Author

Created as part of the Python Daily Challenge, Section 06.