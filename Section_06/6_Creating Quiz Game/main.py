# Import the random module for shuffling questions
import random

# Define the constant for quiz file name
QUIZ_FILE = 'quiz.txt'

def load_quiz_data(filename):
    """Load and parse quiz questions from a file."""
    try:
        # Open the file with UTF-8 encoding to support special characters
        with open(filename, 'r', encoding='utf-8') as file:
            # Initialize empty list to store questions
            questions = []
            # Iterate through each line in the file
            for line in file:
                # Split line by '|' and remove whitespace from each part
                parts = [part.strip() for part in line.strip().split('|')]
                # Check if line has at least 5 parts (question + 4 options + answer)
                if len(parts) >= 5:  
                    # Extract the question from first part
                    question = parts[0]
                    # Extract the 4 options from next parts
                    options = parts[1:5]
                    # Get the correct answer
                    correct_answer = parts[4]
                    # Add tuple of (question, options, answer) to questions list
                    questions.append((question, options, correct_answer))
            # Return all loaded questions
            return questions
    except FileNotFoundError:
        # Print error message if file doesn't exist
        print(f"Error: File '{filename}' not found.")
        # Return empty list if file not found
        return []

def ask_question(question, options, correct_answer):
    """Display a single question and handle user input."""
    # Print the question with a newline before it
    print(f"\n{question}")
    # Print each option with a number (1-4)
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

    # Keep asking until valid answer is given
    while True:
        try:
            # Get user's numeric choice and convert to integer
            choice = int(input("Enter your answer (1-{}): ".format(len(options))))
            # Validate if choice is within valid range
            if 1 <= choice <= len(options):
                # Get the selected answer text
                selected = options[choice - 1]
                # Compare selected answer with correct answer (case-insensitive)
                if selected.strip().lower() == correct_answer.strip().lower():
                    # Print success message if correct
                    print("✅ Correct!")
                    return True
                else:
                    # Print failure message and show correct answer
                    print(f"❌ Wrong! Correct answer: {correct_answer}")
                    return False
            else:
                # Print error for out-of-range number
                print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            # Print error for non-numeric input
            print("Invalid input. Please enter a valid number.")

def run_quiz(questions):
    """Run through all quiz questions and calculate the score."""
    # Check if questions list is empty
    if not questions:
        print("No quiz data available.")
        return

    # Randomize the order of questions
    random.shuffle(questions)
    # Initialize score counter
    score = 0

    # Loop through each question tuple
    for question, options, correct_answer in questions:
        # Increment score if answer is correct
        if ask_question(question, options, correct_answer):
            score += 1

    # Print final score with emoji
    print(f"\n🎯 Your Score: {score}/{len(questions)}")

def play_quiz():
    """Main game loop."""
    # Display welcome message
    print("🧠 Welcome to the Python ML Quiz Game!")

    # Load questions from file
    questions = load_quiz_data(QUIZ_FILE)
    # Exit if no questions loaded
    if not questions:
        return

    # Main game loop
    while True:
        # Run one round of the quiz
        run_quiz(questions)
        # Ask if player wants to play again
        retry = input("\nPlay again? (yes/no): ").strip().lower()
        # Exit if answer is not 'yes' or 'y'
        if retry not in ['yes', 'y']:
            # Show goodbye message
            print("👋 Thanks for playing! Goodbye!")
            break

# Check if this file is run directly (not imported)
if __name__ == '__main__':
    # Start the quiz game
    play_quiz()
