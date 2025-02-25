print("---------------- Day 02 ----------------")
# 🚀 Challenge: Aisa Python program likhna hai jo user se ek sentence le aur usme jitne words hain, count kare! 🔢💡  
# 🔥 For Example:  
# 📌 Input: "Python is amazing!"  
# 📌 Output: Total words: 3  
# 💡 Hint: 
# - split() function ka use karke sentence ko words me tod sakte ho.  
# - len() function se words ki total count nikal sakte ho.  

user_input = input("Enter a sentence:") 
words = user_input.split() # split() function ka use karke sentence ko words me tod sakte hain.
print("Total words:", len(words)) # len() function se words ki total count nikal sakte hain.
