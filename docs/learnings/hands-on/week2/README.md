# Week 2 Hands-on Exercise: Vocabulary Data Analysis Tasks

## 🎯 Exercise Overview
Build on your Week 1 vocabulary project by analyzing vocabulary data using pandas, numpy, and matplotlib. This prepares you for AI/ML workflows starting in Week 3.

## 📊 Setup: Create Your Dataset

Create a CSV file called `vocabulary_extended.csv` with these columns:
- `english` - English word
- `german` - German translation
- `category` - Word category (fruit, object, emotion, action, adjective, technology, animal, nature)
- `difficulty` - Difficulty level (1-5, where 1 is easiest)
- `frequency_rank` - How common the word is (lower numbers = more common)

Include at least 15 vocabulary entries across different categories and difficulty levels.

---

## 📋 Part 1: Data Loading & Exploration

**Your Tasks:**
1. Load your CSV file using pandas
2. Display basic information about your dataset:
    - Dataset shape (rows, columns)
    - Column names and data types
    - First 5 rows
    - Basic statistical summary
3. Check for any missing values or data quality issues

---

## 📈 Part 2: Data Analysis

**Your Tasks:**
1. **Category Analysis:**
    - Count how many words are in each category
    - Find which category has the most/least words

2. **Difficulty Analysis:**
    - Group words by difficulty level
    - Calculate average frequency rank for each difficulty
    - Count words per difficulty level

3. **Pattern Discovery:**
    - Find the most common (lowest frequency rank) word in each category
    - Identify any correlations between difficulty and frequency
    - Calculate average word length by category

---

## 📊 Part 3: Data Visualization

Create 4 different visualizations:

1. **Bar chart:** Words per category
2. **Scatter plot:** Difficulty level vs. frequency rank
3. **Histogram:** Distribution of English word lengths
4. **Heatmap or grouped chart:** Average frequency by category and difficulty

Save your visualizations as a single image file.

---

## 🔍 Part 4: Advanced Analysis

**Your Tasks:**
1. **Text Processing Prep:**
    - Convert all words to lowercase
    - Analyze character frequency in English words
    - Find words that contain specific letter patterns

2. **Learning Recommendations:**
    - Create a list of "beginner-friendly" words (difficulty ≤ 2, sorted by frequency)
    - Suggest an optimal learning order based on difficulty and frequency

3. **Data Quality Checks:**
    - Check for duplicate words
    - Validate that difficulty levels are within expected range (1-5)
    - Ensure frequency ranks make sense

---

## 💾 Part 5: Export & Documentation

**Your Tasks:**
1. Create a summary report with:
    - Total number of words
    - Number of categories
    - Average difficulty level
    - Most common category
    - Data quality metrics

2. Export your enhanced dataset as:
    - Updated CSV file with any new calculated columns
    - JSON summary report

3. Document your findings in comments or a separate text file

---

## 🏆 Bonus Challenges (Optional)

If you finish early, try these:

1. **Data Expansion:** Add 10 more vocabulary entries with realistic difficulty and frequency values
2. **Smart Recommendations:** Create a function that recommends next words to learn based on current progress
3. **Advanced Visualizations:** Create an interactive plot or dashboard view
4. **Data Validation:** Build checks to ensure new vocabulary entries have consistent formatting
5. **Multi-format Export:** Export your data as Excel, JSON, and pickle formats

---

## 📚 Required Libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import json
```

- pandas: For loading, cleaning, exploring, and analyzing tabular data (CSV files, grouping, aggregations).
- numpy: For efficient numerical operations and calculations, often used with pandas for advanced stats.
- matplotlib.pyplot: For creating visualizations (bar charts, scatter plots, histograms, heatmaps).
- collections (e.g., Counter): For counting elements, such as character frequencies in words.
- json: For exporting summary reports and data in JSON format, as required in the export/documentation step.

## ⏰ Time Allocation
- **Day 1 (45 min):** Parts 1-2 (Loading & Analysis)
- **Day 2 (60 min):** Parts 3-4 (Visualization & Advanced Analysis)
- **Day 3 (30 min):** Part 5 + Documentation

## 🎯 Learning Goals
By completing this exercise, you will:
- ✅ Master pandas DataFrame operations
- ✅ Create meaningful data visualizations
- ✅ Understand data quality and validation
- ✅ Practice the data science workflow
- ✅ Prepare data structures for AI/ML applications
- ✅ Build portfolio-ready analysis project