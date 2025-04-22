# Birthday Reminder
from datetime import datetime  # Importing the datetime module to work with dates


def store_birthdays():
    """
    Function to store birthdays in a dictionary.
    Allows the user to input names and their corresponding birthdays.
    """
    birthdays: dict = {}  # Initialize an empty dictionary to store birthdays

    while True:
        name = input('Enter name (or "q" to quit): ')  # Prompt user for a name
        if name.lower() == 'q':  # Exit the loop if the user enters 'q'
            break
        # Prompt user for the birthday date in DD-MM-YYYY format
        birthday_date = input(f"Enter {name}'s birthday (DD-MM-YYYY): ")
        birthdays[name] = birthday_date  # Store the name and birthday in the dictionary
    return birthdays  # Return the dictionary of birthdays


def check_birthdays(birthdays):
    """
    Function to check if today is someone's birthday.
    Compares today's date with the stored birthdays.
    """
    today = datetime.today().strftime('%d-%m-%Y')  # Get today's date in DD-MM-YYYY format
    for name, birthday in birthdays.items():  # Iterate through the stored birthdays
        if birthday == today:  # Check if the birthday matches today's date
            print(f"Today is {name}'s birthday!")  # Print a birthday message
            return  # Exit the function after finding a match
    print("No birthdays today.")  # Print a message if no birthdays match


def main():
    """
    Main function to run the Birthday Reminder program.
    Handles storing and checking birthdays.
    """
    print('\n🎂 Birthday Reminder 🎈\n')  # Display a welcome message
    our_birthdays = store_birthdays()  # Call the function to store birthdays
    check_birthdays(our_birthdays)  # Call the function to check for today's birthdays


if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly


