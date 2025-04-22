#!/usr/bin/env python3
"""
Mad Libs Game
This is a simple implementation of the classic Mad Libs word game where players 
input different types of words that are then used to complete a story template.
"""

def mad_libs():
    """
    Main game function that collects user input and generates a story.
    Prompts the user for various parts of speech and combines them into a predefined story template.
    """
    # Display welcome message
    print("Welcome to Mad Libs Game!")

    # Collect various parts of speech from the user
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    noun2 = input("Enter another noun: ")

    # Create the story using string formatting with the collected words
    story =f"Today, I went to the {adjective1} {noun1} and saw a {adjective2} {noun2}. I decided to {verb1} it!"

    # Display the completed story
    print("\nHere's your story:\n")
    print(story)

def main():
    """
    Main function that serves as the entry point of the program.
    """
    mad_libs()

# Standard boilerplate to call the main() function
if __name__ == "__main__":
    main()