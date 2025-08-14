# Create a file "vocabulary.txt" with this format:
# apple,Apfel,fruit
# book,Buch,object
# happy,glücklich,emotion
# run,rennen,action

# Project tasks:
# 1. Read and parse file
# 2. Group by categories
# 3. Output statistics (count per category)
# 4. Implement search function
# 5. Allow adding new vocabulary

file = 'vocabulary.txt'
handle = open(file, 'r', encoding='utf-8')

categories = {}

for line in handle:
    words = line.strip().split(',')
    if len(words) >= 3:
        english_word = words[0]
        german_word = words[1]
        category = words[2]

        if category not in categories:
            categories[category] = []

        categories[category].append({
            'english': english_word,
            'german': german_word
        })

handle.close()

print("\nStatistics:")
for category, vocab_list in categories.items():
    print(f"\n{category}: {len(vocab_list)} words")
    for vocab in vocab_list:
        print(f"  {vocab['english']} -> {vocab['german']}")