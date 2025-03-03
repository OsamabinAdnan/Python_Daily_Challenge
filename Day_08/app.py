import random
from colorama import Fore, Style

# Step 1: Generate a random number between 1 and 100
random_number = random.randint(1, 100)

print(Fore.LIGHTRED_EX + "\n🎉 Welcome to the Number Guessing Game! 🎉")
print(Fore.LIGHTGREEN_EX + "I have selected a number between 1 and 100. Try to guess it!\n")

# Step 2: Loop until the user guesses the correct number
while True:
    try:
        # Step 3: Take user input
        user_input = int(input(Fore.YELLOW + "\nEnter your guess: " + Style.RESET_ALL))

        # Step 4: Check if the guess is correct
        if user_input == random_number:
            print(Fore.GREEN + "\nCongratulations! You guessed the correct number:"+ Style.RESET_ALL, random_number)
            break # Exit the loop since the user guessed correctly
        elif user_input < random_number:
            print(Fore.RED + "\nToo low! Try again."+ Style.RESET_ALL)
        else:
            print(Fore.BLUE + "\nToo high! Try again." + Style.RESET_ALL)
    except ValueError:
        print(Fore.MAGENTA + "\nInvalid input. Please enter a valid number."+ Style.RESET_ALL)