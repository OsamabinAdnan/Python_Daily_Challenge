# text: The message to be encrypted.
# shift: The number of positions each letter should be moved forward (default = 3).
def encrypt(text, shift=3):
    """Encrypts the given text using Caesar Cipher with the specified shift."""
    encrypted_text = ""  # Initialize an empty string to store the encrypted text
    
    for char in text:  # Loop through each character in the input text

        if char.isalpha():  # Check if the character is a letter (ignores spaces & symbols) | Non-alphabet characters (e.g., spaces, numbers, punctuation) remain unchanged.

            # If char.isupper(), it uses ord('A') as the ASCII base.
            # Otherwise, it uses ord('a') for lowercase letters.
            shift_base = ord('A') if char.isupper() else ord('a')  # Get ASCII base for upper/lowercase

            # Converts the letter into its ASCII code using ord().
            # Subtracts the ASCII base (shift_base) to normalize A-Z or a-z to 0-25 range.
            # Adds the shift value.
            # Uses % 26 to wrap around if the letter goes past 'Z' or 'z'.
            # Converts it back to a character using chr().
            # Adds the encrypted letter to encrypted_text.
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)  # Shift the character
        else:
            # If the character is not a letter, it is added unchanged to the encrypted_text.
            encrypted_text += char  # Keep non-alphabet characters unchanged
    
    return encrypted_text  # Return the encrypted text

# Defines the function decrypt() which reverses the encryption.
def decrypt (text, shift=3):
    """Decrypts the given text by shifting letters back."""
    # Use the same function with a negative shift to decrypt
    # Instead of writing a new function, it reuses encrypt() but with a negative shift to reverse the encryption.
    return(encrypt(text, -shift))

def main():
    """Main function to run the encryption/decryption tool."""
    # Displays a welcome message.
    print("🔒 Welcome to the Caesar Cipher Encryption & Decryption Tool! 🔑")  # Display welcome message

    while True:  # Infinite loop to keep the program running until the user exits
        # Displays a menu for the user to select an option.
        print("\nChoose an option:")  
        print("1. Encrypt a message")  
        print("2. Decrypt a message")  
        print("3. Exit")  

        # Asks the user to input their choice.
        choice = input("Enter your choice (1/2/3): ")  # Get user input for menu selection

        # If the user chooses option 1, proceed with encryption.
        if choice == '1':  # If user chooses encryption
            message = input("Enter the message to encrypt: ")  # Prompts the user to enter the message they want to encrypt.
            shift = int(input("Enter shift value (default is 3): ") or 3)  # Ask for shift value, If the user presses Enter without input, it defaults to 3.
            encrypted_msg = encrypt(message, shift)  # Calls the encrypt() function with the message and shift value.
            print(f"🔐 Encrypted Message: {encrypted_msg}")  # Display encrypted message

        # If the user chooses option 2, proceed with decryption.
        elif choice == '2':  # If user chooses decryption
            message = input("Enter the message to decrypt: ")  # Prompts the user to enter the encrypted message.
            shift = int(input("Enter shift value used for encryption: ") or 3)  # Asks the user for the same shift value that was used for encryption.
            # Calls the decrypt() function with the encrypted message and shift value.
            decrypted_msg = decrypt(message, shift)  # Decrypt the message
            print(f"🔓 Decrypted Message: {decrypted_msg}")  # Display decrypted message

        # If the user chooses option 3, the program exits.
        elif choice == '3':  # If user chooses to exit
            print("🔚 Exiting the program. Goodbye!")  # Display exit message
            break  # Exit the loop and end the program
        
        # If the user enters an invalid choice, it asks them to try again.
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")  # Handle invalid input

main()