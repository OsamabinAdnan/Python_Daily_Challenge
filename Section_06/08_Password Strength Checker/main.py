# Import the 're' module for regular expression matching
import re

# Function to check the strength of a password
def check_password_strength(password):
    # Initialize strength score
    strength = 0

    # Initialize a list to store improvement suggestions
    suggestions = []

    # Check if the password length is at least 8 characters
    if len(password) >= 8:
        strength += 1  # Good length, increase strength
    else:
        suggestions.append("Password must be at least 8 characters long.")  # Suggest improvement

    # Check for at least one uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1  # Contains uppercase letter
    else:
        suggestions.append("Password must contain at least one uppercase letter.")

    # Check for at least one lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1  # Contains lowercase letter
    else:
        suggestions.append("Password must contain at least one lowercase letter.")

    # Check for at least one digit
    if re.search(r'[0-9]', password):
        strength += 1  # Contains a number
    else:
        suggestions.append("Password must contain at least one digit")

    # Check for at least one special character (from a predefined set)
    if re.search(r'[!@#$%^&*()_+-?><;:|<>.,{}]', password):
        strength += 1  # Contains special character
    else:
        suggestions.append('Password must contain at least one special character')

    # Return the strength score and the list of suggestions
    return strength, suggestions

# Main function to handle user interaction
def main():
    # Prompt the user to enter a password
    password = input("\nEnter your password: ")

    # Check password strength and receive feedback
    strength, suggestions = check_password_strength(password)

    # Display strength score out of 5
    print(f'\nPassword Strength: {strength}/5')

    # If the password is not perfect, show suggestions
    if strength < 5:
        print('\nSuggestions to improve your password:')
        for suggestion in suggestions:
            print(f'- {suggestion}')
    else:
        # If password meets all criteria
        print('Your password is strong enough!\n')

# Entry point: runs only if this file is executed directly
if __name__ == "__main__":
    main()
