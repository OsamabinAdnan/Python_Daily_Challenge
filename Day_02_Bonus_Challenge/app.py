# 💡 Bonus Challenge (Optional) 🤩

# Agar tumhe extra challenge chahiye, to same program ko aise modify karo ke words ko reverse order me print kare! 🔄  

# 📌 Example:  
# 🔹 Input: "I love Python"  
# 🔹 Output: "Python love I"  

user_input = input("Enter a sentence: ") # This line prompts the user to enter a sentence and stores it as a string in the variable user_input.
reversed_words = user_input.split()[::-1] # user_input.split() converts the sentence into a list of words by splitting at spaces. | [::-1] reverses the list.
print("Reversed sentence:"," ".join(reversed_words)) # " ".join(reversed_words) joins the reversed words back into a single string with spaces between them.