import tkinter as tk # GUI library for desktop applications
import random # Used to select a random question
import json # For saving/loading flashcards from a file
import os # To check if a file exists

# Default flashcards (used if no file is found)
flashcards = {
    "What is the output of `print(2 ** 3)`?": "8",
    "What keyword is used to define a function in Python?": "`def`",
    "What data type is the result of: `len('hello')`?": "`5`",
    "What is the keyword to create a class in Python?": "`class`",
}

# Save flashcards to a JSON file
def save_flashcards():
    with open('flashcards.json', 'w') as file:
        json.dump(flashcards, file)

# Load flashcards from a JSON file if it exists, otherwise use the default set
def load_flashcards(filename = 'flashcards.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return flashcards # fallback to default data


# Define the FlashcardApp class using tkinter
class FlashcardApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Python Flashcards') # Set the title of the window
        self.data = load_flashcards() # Load the flashcards
        self.question, self.answer = None, None # Initialize question and answer variables
    

        # Display for the question
        self.question_label = tk.Label(
            master, text = 'Click Next for a question',
            font=('Arial', 16, 'bold'), wraplength=400
        )
        self.question_label.pack(pady=20)

        # Display for the answer (initially blank)
        self.answer_label = tk.Label(
        master, text="", font=('Arial', 14), fg="blue", wraplength=400
        )
        self.answer_label.pack(pady=10)

        # Button to get a new question
        self.next_button = tk.Button(
            master, text="Next Question", command=self.show_question
        )
        self.next_button.pack(pady=5)

        # Button to reveal the answer
        self.show_button = tk.Button(
            master, text="Show Answer", command=self.show_answer
        )
        self.show_button.pack(pady=5)

    # Pick and show a random question
    def show_question(self):
        self.question, self.answer = random.choice(list(self.data.items()))
        self.question_label.config(text=f"Question: {self.question}")
        self.answer_label.config(text="")  # Clear previous answer

    # Show the answer to the current question
    def show_answer(self):
        self.answer_label.config(text=f"Answer: {self.answer}")

# Start the tkinter GUI application
if __name__ == "__main__":
    root = tk.Tk()             # Create the root window
    app = FlashcardApp(root)   # Instantiate the app
    root.mainloop()            # Start the event loop
