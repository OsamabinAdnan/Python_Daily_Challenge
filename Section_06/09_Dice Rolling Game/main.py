# Import the random module to simulate dice rolling
import random

# Function to simulate rolling a six-sided die
def roll_dice():
    # Returns a random integer between 1 and 6 (inclusive)
    return random.randint(1, 6)

# Main function to run the dice roller simulator
def main():
    # Print welcome message
    print('\nDice Roller Simulator')
    print('---------------------\n')

    # Loop to allow multiple dice rolls until user chooses to stop
    while True:
        # Call the roll_dice function and display the result
        print(f'You rolled: {roll_dice()}')
        
        # Ask the user if they want to roll again, converting input to lowercase
        count = input('Roll again? (yes/no): ').lower()

        # If the user types anything other than "yes", exit the loop
        if count != 'yes':
            print('\n👋 Goodbye!\n')
            break

# Only run the main function if this script is executed directly
if __name__ == '__main__':
    main()
