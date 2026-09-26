# 🔄 Python Palindrome Checker

A lightweight, efficient Python script that checks whether a given string, number, or phrase is a palindrome (reads the same backward as forward). 

This project demonstrates core string manipulation techniques, data cleaning using regular expressions, and basic algorithm design in Python.

---

## 🛠️ Tech Stack & Concepts
* **Language:** Python 3.x
* **Core Concepts:** String Slicing, Regular Expressions (`re`), Control Flow, Functions, Two-Pointer Technique

---

## 📌 Features
* **Case-Insensitive Check:** Handles mixed upper and lowercase letters seamlessly (e.g., `"Racecar"` $\rightarrow$ Valid).
* **Phrase Support:** Automatically strips out spaces, punctuation, and special characters to validate complex phrases (e.g., `"A man, a plan, a canal: Panama"` $\rightarrow$ Valid).
* **Multi-Input Support:** Accepts both text strings and numeric values.

---

## 💡 Key Learnings & Engineering Insights
* **String Sanitization:** Learned how to use Python's built-in `re.sub()` function to clean raw user inputs before running algorithmic checks.
* **Optimization (Slicing vs. Two-Pointer):** 
  * Explored Pythonic extended slicing (`string[::-1]`) for rapid $O(N)$ checks.
  * Implemented an iterative two-pointer approach to optimize memory performance on long strings.
* **Edge Case Handling:** Addressed edge cases such as empty inputs, single-character inputs, and inputs containing only symbols/spaces.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/palindrome-checker.git](https://github.com/YOUR-USERNAME/palindrome-checker.git)
   cd palindrome-checker
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```

---

## 🔮 Future Improvements
* [ ] Add a graphical user interface (GUI) using Tkinter or PySimpleGUI.
* [ ] Convert the script into a web app using Flask or Streamlit.
* [ ] Implement unit tests using Python's `unittest` module.