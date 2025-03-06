import re  # Importing the 're' module for regular expressions

def clean_word(word):
    """
    Cleans the input word by:
    - Converting to lowercase
    - Removing spaces
    - Removing special characters and numbers
    """

    word = word.lower()  # Convert the word to lowercase to ensure case insensitivity
    word = re.sub(r'[^a-z]', '', word)  # Remove everything except lowercase alphabets (removes numbers & special characters)
    word = word.replace(" ", "")  # Remove any remaining spaces (though regex already handles it)
    return word  # Return the cleaned word

def is_anagram(word1, word2):
    """
    Checks if two words are anagrams after cleaning them.
    - An anagram means both words contain the same letters but in a different order.
    """

    word1 = clean_word(word1)  # Clean the first word (convert to lowercase & remove unwanted characters)
    word2 = clean_word(word2)  # Clean the second word

    return sorted(word1) == sorted(word2)  # Compare sorted letters of both words to check if they are anagrams

# Taking user input for the words
word1 = input("Enter the first word: ")  # Ask the user to input the first word
word2 = input("Enter the second word: ")  # Ask the user to input the second word

# Check if the words are anagrams and print the result
if is_anagram(word1, word2):
    print(f"\n{word1} and {word2} are anagrams. ✅")  # Print confirmation if they are anagrams
else:
    print(f"\n{word1} and {word2} are not anagrams. ❌")  # Print message if they are not anagrams
