import re # The re module (regular expressions) is imported to help detect special characters in the password.

def check_password_strenght(password):
    if len(password) < 6 or password.isalpha() or password.isnumeric():
        return "Weak Password ❌"
    
    if len(password) >= 8:
        # Checks if the password contains at least one uppercase letter.
        has_uppercase = any(char.isupper() for char in password)
        # Checks if the password contains at least one lowercase letter.
        has_lowercase = any(char.islower() for char in password)
        # Checks if the password contains at least one number.
        has_digit = any(char.isdigit() for char in password)
        # Uses regular expressions (re.search) to check if the password contains at least one special character.
        has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

        if has_uppercase and has_lowercase and has_digit and has_special:
            return "Strong Password ✅"
        else:
            return "Moderate Password 🟡"
    else:
        return "Weak Password ❌"

password = input("Enter your password: ")
strength = check_password_strenght(password)
print("Password Strength:", strength)
