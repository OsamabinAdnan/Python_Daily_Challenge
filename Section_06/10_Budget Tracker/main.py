# Import the JSON module to handle reading and writing data in JSON format
import json

# Define the filename where budget data will be stored
FILENAME = 'budget.json'

# Function to load the budget from a JSON file
def load_budget():
    try:
        # Attempt to open the file in read mode
        with open(FILENAME, 'r') as file:
            # Load the JSON content into a Python dictionary and return it
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is corrupt, return a default empty budget
        return {'income': [], 'expenses': []}

# Function to save the current budget to the JSON file
def save_budget(budget):
    # Open the file in write mode and dump the dictionary as JSON
    with open(FILENAME, 'w') as file:
        json.dump(budget, file)

# Function to add a new income or expense entry
def add_entry(budget, entry_type):
    # Prompt the user to enter the amount (converted to float for calculations)
    amount = float(input(f"Enter the amount for {entry_type}: "))
    # Append the amount to the appropriate list ('income' or 'expenses')
    budget[entry_type].append(amount)
    # Save the updated budget to the file
    save_budget(budget)
    # Confirm successful addition to the user
    print(f'{entry_type.capitalize()} added successfully!')

# Function to display the current budget summary
def display_budget(budget):
    # Calculate the total income by summing the 'income' list
    total_income = sum(budget['income'])
    # Calculate the total expenses by summing the 'expenses' list
    total_expenses = sum(budget['expenses'])
    # Calculate the remaining balance
    balance = total_income - total_expenses

    # Print the budget summary to the console
    print(f'\nTotal Income: {total_income}')
    print(f'Total Expenses: {total_expenses}')
    print(f'Balance: {balance}')

# Main function to run the Budget Tracker CLI application
def main():
    # Load the budget from file (or use a default empty one)
    budget = load_budget()

    # Loop to repeatedly show the menu until user chooses to exit
    while True:
        # Display the menu options
        print("\n💰 Budget Tracker:")
        print("1. Add Income")
        print("2. Add Expenses")
        print("3. Display Budget")
        print("4. Exit")

        # Get the user's menu choice
        choice = int(input("Enter your choice (1/2/3/4): "))

        # Execute the appropriate function based on the user's choice
        if choice == 1:
            add_entry(budget, 'income')
        elif choice == 2:
            add_entry(budget, 'expenses')
        elif choice == 3:
            display_budget(budget)
        elif choice == 4:
            # Exit the application
            print("Exiting Budget Tracker. Goodbye! 👋\n")
            break
        else:
            # Inform the user about invalid input
            print("Invalid choice. Please choose from given options (1/2/3/4).\n")

# Ensure that the script runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
