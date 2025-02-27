# 1st Method

# Importing the inflect library: This library is used for number-to-word conversion in English.
import inflect

from colorama import Fore, Style

# The inflect.engine() function initializes the inflect object, which provides access to various language functions.
p = inflect.engine()

# p.number_to_words(num) converts the number into its word representation.
num = int(input ("Enter a number: "))

words = p.number_to_words(num)

print(Fore.GREEN + "The number in words is: "+ Fore.LIGHTYELLOW_EX + words + Style.RESET_ALL)