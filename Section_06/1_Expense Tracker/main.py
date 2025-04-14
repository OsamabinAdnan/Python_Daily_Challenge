import csv
from datetime import datetime

# File name for storing the data
FILENAME = 'expense_data.csv'

# Function to add a expense
def add_expense():
    """
    This function prompts the user to enter the date, category, description and amount of the expense.
    It then appends the expense data to the CSV file.
    """
    try:
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Travel, Groceries etc.): ")
        description = input('Enter a short description: ')
        amount = float(input("Enter the amount: "))

        # save expense data to CSV file
        with open(FILENAME, mode='a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category,description, amount])
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

# Function to view expenses
def view_expenses():
    """
    This function reads the expense data from the CSV file and displays it in a tabular format.
    """
    try:
        with open(FILENAME, mode= 'r') as file:
            reader = csv.reader(file)
            print(f'\n{'Date':<12} | {"Category":<20} | {"Description":<50} | {"Amount":>10}')
            print('_' * 100)
            for row in reader:
                print(f'{row[0]:<12} | {row[1]:<20} | {row[2]:<50} | {row[3]:<10}')
    except FileNotFoundError:
        print("No expenses found!")

def main():
    """
    This is the main function that displays a menu and prompts the user to choose an option.
    Based on the user's choice, it calls the corresponding function.
    """
    while True:
        print('\nExpense Tracker Menu:')
        print('1. Add Expense')
        print('2. View Expenses')
        print('3. Exit')

        choice = input('Enter your choice (1/2/3):')

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

# Call the main function
if __name__ == '__main__':
    main()