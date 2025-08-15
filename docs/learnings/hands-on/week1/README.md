# Week 1 Hands-on Exercise: Vocabulary File Manager

## 🎯 Exercise Overview
Build a Python program that manages English-German vocabulary pairs from a text file. This project teaches core Python concepts while creating a foundation for your future English learning app.

## 📝 Setup: Create Your Data File

Create a text file called `vocabulary.txt` with this format:
```
apple,Apfel,fruit
book,Buch,object
happy,glücklich,emotion
run,rennen,action
beautiful,schön,adjective
learn,lernen,action
cat,Katze,animal
```

Each line contains: `english_word,german_word,category`

Start with at least 10 vocabulary entries across different categories.

---

## 📋 Part 1: File Reading & Basic Processing

**Your Tasks:**
1. **Read the File:**
    - Open and read `vocabulary.txt`
    - Handle potential file errors gracefully
    - Split each line into components (English, German, category)

2. **Data Validation:**
    - Check that each line has exactly 3 parts
    - Remove any empty lines
    - Print how many valid entries were loaded

3. **Display Data:**
    - Print all vocabulary entries in a formatted way
    - Show a count of total entries loaded

---

## 📊 Part 2: Data Organization & Analysis

**Your Tasks:**
1. **Categorize Words:**
    - Group words by category
    - Count how many words are in each category
    - Display the results sorted by category name

2. **Search Functionality:**
    - Ask user to input an English word
    - Find and display the German translation and category
    - Handle cases where the word is not found

3. **Statistics:**
    - Find the category with the most words
    - Calculate average word length for English words
    - Count words that contain specific letters (e.g., all words with 'a')

---

## ✏️ Part 3: Adding New Vocabulary

**Your Tasks:**
1. **Add New Entries:**
    - Ask user for: English word, German translation, category
    - Validate that all fields are provided
    - Add the new entry to your data structure

2. **Duplicate Checking:**
    - Check if English word already exists
    - If duplicate, ask user if they want to update or skip

3. **Save Changes:**
    - Write updated vocabulary back to file
    - Maintain the same format
    - Confirm successful save to user

---

## 🔍 Part 4: Advanced Features

**Your Tasks:**
1. **Menu System:**
    - Create a simple menu with options:
        - View all vocabulary
        - Search for word
        - Add new word
        - Show statistics
        - Exit program

2. **Enhanced Search:**
    - Search by German word (reverse lookup)
    - Search by category (show all words in category)
    - Partial word matching (find words containing substring)

3. **Data Export:**
    - Save vocabulary by category to separate files
    - Create a summary report with statistics
    - Export in different formats (maybe as organized text)

---

## 🏆 Bonus Challenges (Optional)

If you finish early, try these:

1. **Random Quiz Mode:** Pick random words and test translations
2. **Word Sorting:** Sort vocabulary alphabetically by English or German
3. **Backup System:** Create dated backup files when saving
4. **Input Validation:** Ensure categories follow a predefined list
5. **Case Handling:** Make searches case-insensitive
6. **File Format Flexibility:** Handle different delimiters (comma, semicolon, tab)

---

## 📚 Python Concepts You'll Use
- File I/O (`open()`, `read()`, `write()`)
- String manipulation (`split()`, `strip()`, `lower()`)
- Lists and dictionaries
- Loops (`for`, `while`)
- Conditionals (`if`, `elif`, `else`)
- Functions (organize your code)
- Error handling (`try`, `except`)
- User input (`input()`)

## ⏰ Time Allocation
- **Day 1 (45 min):** Part 1 (File Reading & Basic Processing)
- **Day 2 (45 min):** Part 2 (Data Organization & Analysis)
- **Day 3 (45 min):** Part 3 (Adding New Vocabulary)
- **Day 4 (45 min):** Part 4 (Advanced Features)
- **Day 5 (30 min):** Bonus challenges & code cleanup

## 🎯 Learning Goals
By completing this exercise, you will:
- ✅ Master Python file operations
- ✅ Work with strings, lists, and dictionaries
- ✅ Implement user interaction and input validation
- ✅ Practice error handling and edge cases
- ✅ Build a complete, functional program
- ✅ Create your first portfolio project
- ✅ Establish groundwork for your English learning app

## 📖 Testing Your Program

Test these scenarios:
- Empty vocabulary file
- File with invalid entries (missing commas, extra fields)
- Searching for non-existent words
- Adding duplicate words
- Categories with no words
- Very long word entries

## 💡 Success Criteria
Your program should:
- Handle errors without crashing
- Maintain data consistency when saving
- Provide clear user feedback
- Be easy to use and understand
- Work with different vocabulary file sizes
- Be ready to extend with new features

---

## 🚀 Connection to Your Goals
This exercise directly supports your English learning app by:
- **Data Management:** Core functionality for storing vocabulary
- **Search Features:** Foundation for word lookup in your app
- **User Interaction:** Practice for chatbot interfaces
- **File Handling:** Skills needed for saving user progress
- **Error Handling:** Essential for robust app development