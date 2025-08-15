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

def read_vocabularies(file):
    categories = {}
    handle = open(file, 'r', encoding='utf-8')

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
    return categories

def print_statistics(categories):
    print("\nStatistics:")
    for category, vocab_list in categories.items():
        print(f"\n{category}: {len(vocab_list)} words")
        for vocab in vocab_list:
            print(f"  {vocab['english']} -> {vocab['german']}")

def search_vocabulary(categories, search):
    results = []
    search = search.lower()

    for category, vocab_list in categories.items():
        for vocab in vocab_list:
            if (search in vocab['english'].lower() or
                    search in vocab['german'].lower()):
                results.append({
                    'english': vocab['english'],
                    'german': vocab['german'],
                    'category': category
                })

    if results:
        print(f"\nFound result for '{search}':")
        for result in results:
            print(f"{result['english']} ({result['german']}) - Category: {result['category']}")
    else:
        print(f"\nNo results found for '{search}'.")

def add_vocabulary(categories, english, german, category):
    if category not in categories:
        categories[category] = []

    categories[category].append({
        'english': english,
        'german': german
    })
    print(f"Added: {english} -> {german} (Category: {category})")

sorted_categories = read_vocabularies('vocabulary.txt')
print_statistics(sorted_categories)

quitting = False
while not quitting:
    user_choice = input("\nWhat do you want to do? (s: search, a: add, q: quit): ").lower()
    if user_choice == 's':
        search_term = input("\nEnter a word to search (in English or German): ")
        search_vocabulary(sorted_categories, search_term)
    elif user_choice == 'a':
        print("\nAdd a new vocabulary")
        new_english = input("English word: ")
        new_german = input("German word: ")
        new_category = input("Category: ")
        add_vocabulary(sorted_categories, new_english, new_german, new_category)
        print_statistics(sorted_categories)
    elif user_choice == 'q':
        print("Exiting the program.")
        quitting = True