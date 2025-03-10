# 🚀 Day 12 – Daily Python Challenge 🐍  

## 🎯 Challenge: Create a Password Strength Checker  
Develop a program that takes a password from the user and analyzes its strength. 💡  

## 🔑 Rules:  
✔ **Weak Password:** Less than 6 characters  
✔ **Medium Password:** 6-10 characters, at least one digit  
✔ **Strong Password:** More than 10 characters, at least one uppercase letter, one digit, and one special character  

## 🔥 Example:  
📌 **Input:** `"Python123"`  
📌 **Output:** `"Strength: Medium"`  

🕒 **Submit your solution before midnight!**  
📌 **Form Link:** [Submit Here](https://forms.gle/oYwxgye44tCxCaGv7)  

---  

## 💡 Hint:  
- Use `len(password)` to check password length.  
- Use `any(char.isdigit() for char in password)` to check for numbers.  
- Use `any(char.isupper() for char in password)` to check for uppercase letters.  
- Use `any(char in "!@#$%^&*()" for char in password)` to check for special characters.  

🚀 **Let’s Go!**  
