# Import the csv module for reading CSV files
import csv

# Import the pyplot module from matplotlib to create visualizations
import matplotlib.pyplot as plt

# Define the name of the CSV file containing the expense data
FILENAME = 'expenses.csv'

# Function to load expenses from the CSV file
def load_expenses():
    try:
        # Open the CSV file in read mode
        with open(FILENAME, 'r') as file:
            # Create a CSV reader object to iterate over lines in the file
            reader = csv.reader(file)
            # Read all rows and return them as a list (including header)
            return [row for row in reader]
    except FileNotFoundError:
        # If the file does not exist, return an empty list
        return []

# Function to categorize expenses and plot a pie chart
def plot_expenses(expenses):
    # Initialize an empty dictionary to store total expenses by category
    categories = {}
    
    # Skip the header row and iterate through the remaining rows in the data
    for row in expenses[1:]:
        # Unpack the row, assuming it's in the format: [date, category, description, amount]
        _, category, _, amount = row
        
        # Convert amount to float and add it to the corresponding category's total
        categories[category] = categories.get(category, 0) + float(amount)
    
    # Create a pie chart of the expense categories
    plt.pie(
        categories.values(),             # Values: total amount per category
        labels=categories.keys(),       # Labels: names of the categories
        autopct='%1.1f%%'               # Display percentages with one decimal place
    )
    
    # Set the title of the pie chart
    plt.title('Expenses by Category')
    
    # Display the pie chart in a new window
    plt.show()

# Main function to load and visualize expenses
def main():
    # Load the expenses from the CSV file
    expenses = load_expenses()
    
    # If any expenses are loaded, plot them
    if expenses:
        plot_expenses(expenses)
    else:
        # If no data is found, print a message to the user
        print('No expenses found.')

# Check if the script is being run directly (not imported)
if __name__ == '__main__':
    # Run the main function
    main()
