from vocabulary_analyzer_base import VocabularyAnalyzerBase

class VocabularyAnalyzerPart2(VocabularyAnalyzerBase):
    def __init__(self, csv_path):
        super().__init__(csv_path)

    def analyze_categories(self):
        print("\n📋 Category Distribution:")
        category_counts = self.df['category'].value_counts()
        print(f"Entries: {dict(category_counts)}")
        print(f"Category with most entries: {category_counts.idxmax()} ({category_counts.max()} entries)")
        idx = self.df.groupby("category")['frequency_rank'].idxmin()
        most_common_word = self.df.loc[idx, ['category', 'english', 'german', 'frequency_rank']]
        print(f"Most common word in each category: {most_common_word.set_index('category')}")
        avg_word_length = self.df.groupby("category")["english"].agg(lambda x: x.str.len().mean())
        print(f"Average word length by category: {avg_word_length}")

    def analyze_difficulty_level(self):
        print("\n📋 Difficulty Level Distribution:")
        difficulty_level_groups = self.df.groupby("difficulty")
        print(f"Total difficulty levels: {difficulty_level_groups.ngroups}")
        print(f"Words by difficulty level: {dict(difficulty_level_groups.size())}")
        print(f"Average frequency by difficulty level: {dict(difficulty_level_groups['frequency_rank'].mean())}")

    def analyze_correlations(self):
        correlations = self.df['difficulty'].corr(self.df['frequency_rank'])
        print("\n📊 Correlation Analysis:")
        print(f"{correlations:.2f}")