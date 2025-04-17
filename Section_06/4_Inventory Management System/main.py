import csv

# Constant for the inventory file name
FILENAME = 'inventory.csv'

def add_item():
    """Add a new item to the inventory CSV file"""
    # Get item details from user
    name = input('Enter the name of item: ')
    quantity = int(input('Enter the quantity of item: '))
    price = float(input('Enter the price of item: '))

    # Open file in append mode and write the new item
    with open(FILENAME, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, quantity, price])
    print('Item added successfully!')

def view_item():
    """Display all items in the inventory"""
    try:
        # Open and read the inventory file
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            # Print header with formatted columns
            print(f"{'Name':<20}{'Quantity':<10}{'Price':<10}")
            print('-' * 40)

            # Print each item's details
            for row in reader:
                print(f"{row[0]:<20}{row[1]:<10}{row[2]:<10}")
    except FileNotFoundError:
        print('File not found!')

def main():
    """Main program loop"""
    while True:
        # Display menu options
        print('\nInventory Management System')
        print('1. Add Item')
        print('2. View Item')
        print('3. Exit')

        # Get user choice
        choices = int(input('Enter your choice (1/2/3): '))

        # Process user choice
        if choices == 1:
            add_item()
        elif choices == 2:
            view_item()
        elif choices == 3:
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

# Entry point of the program
if __name__ == '__main__':
    main()