import string  # Importing the string module to access string constants like punctuation
from colorama import Fore, Style  # Importing Fore and Style from colorama for colored text output

def check_password_strength(password):  # Defining a function to check the strength of a password
    special_characters = string.punctuation  # Getting all special characters from string module

    if len(password) < 6:  # Checking if the password length is less than 6 characters
        return Fore.RED + "Weak Password: should be at least 6 characters long." + Style.RESET_ALL  # Returning a message indicating a weak password
    elif 6 <= len(password) <= 10 and any(char.isdigit() for char in password):  # Checking if the password length is between 6 and 10 characters and contains at least one digit
        return Fore.YELLOW + "Moderate Password: should contain at least one special character." + Style.RESET_ALL  # Returning a message indicating a moderate password
    elif len(password) > 10 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in special_characters for char in password):  # Checking if the password length is greater than 10 characters and contains at least one digit, one uppercase letter, and one special character
        return Fore.GREEN + "Strong Password, your password is secure" + Style.RESET_ALL  # Returning a message indicating a strong password
    else:  # If none of the above conditions are met
        return Fore.CYAN + "Strength: Medium Password" + Style.RESET_ALL  # Returning a message indicating a medium password

password = input("Enter your password:")  # Prompting the user to enter a password
print(f"\nPassword Strength: {check_password_strength(password)}")  # Printing the strength of the entered password