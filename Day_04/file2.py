# 2nd Method

# num2words → Converts numbers to words.
from num2words import num2words
from colorama import Fore, Style

num = int(input("Enter a number: "))

words = num2words(num)

print (Fore.GREEN + "The number in words is: "+ Fore.LIGHTYELLOW_EX + words + Style.RESET_ALL)