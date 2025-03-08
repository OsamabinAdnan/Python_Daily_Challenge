# 📢 Day 11 – Daily Python Challenge 🐍

## 🚀 Challenge: "Emoji Sentiment Analyzer" 🤖😊😢
Today's challenge is fun and useful! You need to write a Python program that analyzes a user's message and detects their mood based on the emojis they use! 🎭💡

## 📌 Task Requirements:
- Take a sentence input from the user.
- Check if the sentence contains emojis.
- If an emoji is found, determine the mood based on the following categories:

  | Emojis        | Detected Mood |
  |--------------|--------------|
  | 😊, 😃, 😍  | "Happy Mood!" 🎉 |
  | 😢, 😭, ☹  | "Sad Mood!" 😢 |
  | 😡, 🤬, 😠  | "Angry Mood!" 😠 |
  | 😐, 😶, 🤔  | "Neutral Mood!" 🤔 |

- If no emoji is found, print: "No emoji found, can't detect mood!" 🤷‍♂

## 📌 Example:

```
Enter your message: I am so happy today! 😊  
Detected Mood: Happy Mood! 🎉  

Enter your message: This is so frustrating! 😡  
Detected Mood: Angry Mood! 😠  

Enter your message: Just another normal day.  
No emoji found, can't detect mood! 🤷‍♂  
```

## 🕒 Submission Deadline
Submit your solution before midnight! ⏳
📌 **Form Link:** [Submit Here](https://forms.gle/oYwxgye44tCxCaGv7)

## 🔥 Let's go! Time to analyze some moods! 🚀

## 📌 Hint:
- Use Python’s `re` module (Regular Expressions) to detect emojis.
- Use a dictionary to map emojis to moods!
- Think about how you can extend this for more emojis in the future. 💡

**To `run` this Streamlit app, write:**  

```python
streamlit run main.py
