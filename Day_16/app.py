def caesar_cipher(text, shift, mode="encrypt"):
    """
    Implements the Caesar cipher encryption/decryption algorithm
    Parameters:
        text (str): The input text to encrypt/decrypt
        shift (int): Number of positions to shift each letter
        mode (str): Either "encrypt" or "decrypt"
    Returns:
        str: The encrypted/decrypted text
    """
    result = ""

    # For decryption, shift in opposite direction by making shift negative
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters separately
            # Get the ASCII base value (65 for 'A', 97 for 'a')
            offset = ord('A') if char.isupper() else ord('a')
            
            # Formula breakdown:
            # 1. ord(char) - offset : Convert letter to 0-25 range
            # 2. + shift : Apply the cipher shift
            # 3. % 26 : Wrap around if shift goes beyond Z/z
            # 4. + offset : Convert back to ASCII value
            new_char = chr((ord(char) - offset + shift) % 26 + offset)
            result += new_char
        else:
            # Preserve spaces, punctuation and other characters
            result += char

    return result

# Get user input
message = input("\nEnter a message: ")
shift_value = int(input("Enter the shift value: "))

# Perform encryption
encrypted_message = caesar_cipher(message, shift_value, mode="encrypt")
print("\nEncrypted:", encrypted_message)

# Perform decryption
decrypted_message = caesar_cipher(encrypted_message, shift_value, mode="decrypt")
print("\nDecrypted:", decrypted_message)
