import random
from word_list import words_list

# Load word from the file
def load_word(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            if not words:
                print("The file is empty. Please add some words in file")
            return words
    except FileNotFoundError:
        print(f"File '{filename}' not found. Please make sure the file exists.")
        return []

# Hangman game logic
def play_hangman(words):
    word = random.choice(words).lower()
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()
    print("\nWelcome to Hangman!")
    print("=" * 20)
    print('\nGuess the word by entering one letter at a time.')
    print('You have 6 attempts to guess the word.')

    while attempts > 0 and '_' in guessed_word:
        print('\nWord:'," ".join(guessed_word))
        print('Attempts left:', attempts)
        print(f'Guessed Letters: {", ".join(sorted(guessed_letters))}')
        guess = input('Enter a letter: ').lower()

        if len(guess) != 1 or not guess. isalpha():
            print('Invalid Input. Please enter a single alphabetical letter.')
            continue
        if guess in guessed_letters:
            print('You have already guessed that letter. Try other letter.')
        elif guess in word:
            print('Correct guess!')
            for i , letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
            guessed_letters.add(guess)
        else:
            print('Incorrect guess!')
            attempts -= 1
            guessed_letters.add(guess)
    if "_" not in guessed_word:
        print('\n⭐ Congratulations! You guessed the word:⭐', word)
    else:
        print('\n😞 Game Over! The word was:', word)

def main():
    words = words_list
    if not words:
        return
    while True:
        play_hangman(words)
        replay = input('\nDo you want to play again? (yes/no): ').lower()
        if replay == 'yes' or replay == 'y':
            continue
        elif replay == 'no' or replay == 'n':
            print('Thanks for playing! Good Bye 👋\n')
            break
        else:
            print('Invalid input! Please enter yes or no.')

if __name__ == "__main__":
    main()
