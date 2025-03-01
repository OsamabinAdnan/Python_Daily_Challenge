from colorama import Fore, Style

user_input = int(input("Enter a number: "))

binary_conversion = bin(user_input)[2:]

print(Fore.YELLOW + f"\nThe binary conversion of {user_input} is {binary_conversion}" +Style.RESET_ALL)

reversed_binary = binary_conversion[::-1]

if binary_conversion == reversed_binary:
    print(Fore.GREEN + f"\nBinary conversion of {user_input} i.e.,{binary_conversion} is a palindrome" + Style.RESET_ALL)
else:
    print(Fore.RED + f"\nBinary conversion of {user_input} i.e., {binary_conversion} is not a palindrome" + Style.RESET_ALL)