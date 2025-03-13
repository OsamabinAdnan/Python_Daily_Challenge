# Create a Random Password Generator!

import random  # Importing the random module for generating random choices
import string  # Importing the string module to get sets of characters

def generate_password(length):
    """
    Generates a secure random password of the given length.

    Args:
    length (int): The desired length of the password.

    Returns:
    str: A randomly generated password with a mix of uppercase, lowercase, digits, and special characters.
    """
    
    # Ensure the password length is at least 6
    if length < 6:
        return "Password length should be at least 6 characters."

    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase  # All lowercase letters (a-z)
    uppercase_letters = string.ascii_uppercase  # All uppercase letters (A-Z)
    digits = string.digits  # All numeric digits (0-9)
    special_characters = string.punctuation  # All special characters (!@#$%^&*...)

    # Ensure the password contains at least one character from each category
    password = [
        random.choice(lowercase_letters),  # Pick one random lowercase letter
        random.choice(uppercase_letters),  # Pick one random uppercase letter
        random.choice(digits),  # Pick one random digit
        random.choice(special_characters),  # Pick one random special character
    ]

    # Create a combined character set including all character types
    all_chars = lowercase_letters + uppercase_letters + digits + special_characters

    # Fill the rest of the password with random characters from all categories
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the password list to randomize character order
    random.shuffle(password)

    # Convert the list into a string and return the final password
    return "".join(password)

# Get user input and generate password
try:
    length = int(input("Enter the desired password length: "))  # Take user input and convert to integer
    print("Generated Password:", generate_password(length))  # Generate and display the password
except ValueError:
    # Handle invalid inputs (non-integer values)
    print("Invalid input. Please enter a valid number.")
