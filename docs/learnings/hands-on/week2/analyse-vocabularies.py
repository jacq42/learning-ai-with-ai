import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class VocabularyAnalyzer:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)

    def analyze_dataset(self):
        print("📊 Dataset Overview:")
        print(f"Shape: {self.df.shape}")
        print(f"Columns: {list(self.df.columns)}")
        dtype_dict = {col: str(dtype) for col, dtype in self.df.dtypes.items()}
        print(f"Datatypes:\n{dtype_dict}")
        print("\nFirst 5 rows:")
        print(self.df.head())

    def analyze_statistics(self):
        aggregation = self.df.agg(
            {
                "difficulty": ["min", "max", "median", "mean"],
                "frequency_rank": ["min", "max", "median", "mean"],
            }
        )
        print("\n📊 Aggregated Statistics:\n")
        print(aggregation)

    def analyze_missing_data(self):
        missing_data = self.df.isnull().sum()
        print("\n🔍 Missing Data Analysis:")
        print(dict(missing_data[missing_data > 0]))
        print("\nMissing Data in line (Index):")
        print(self.df[self.df.isnull().any(axis=1)])

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

    def _plot_words_per_category_ax(self, ax, words_per_category):
        ax.bar(words_per_category.index, words_per_category.values)
        ax.set_title("Number of words per category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Number of words")
        ax.tick_params(axis='x', rotation=45)

    def _plot_difficulty_vs_frequency_ax(self, ax):
        ax.scatter(self.df['difficulty'], self.df['frequency_rank'], alpha=0.7)
        ax.set_title("Difficulty Level vs. Frequency Rank")
        ax.set_xlabel("Difficulty Level")
        ax.set_ylabel("Frequency Rank")

    def _plot_english_word_length_distribution_ax(self, ax):
        word_lengths = self.df['english'].str.len()
        ax.hist(word_lengths, bins=range(word_lengths.min(), word_lengths.max() + 2), edgecolor='black', alpha=0.7)
        ax.set_title("Distribution of English Word Length")
        ax.set_xlabel("Word length")
        ax.set_ylabel("Number of words")

    def _plot_heatmap(self, ax):
        pivot = self.df.pivot_table(
            index='category',
            columns='difficulty',
            values='frequency_rank',
            aggfunc='mean'
        )
        sns.heatmap(pivot, annot=True, fmt=".1f", cmap="YlGnBu")
        ax.set_title("Average Frequency Rank by Category and Difficulty")
        ax.set_xlabel("Difficulty Level")
        ax.set_ylabel("Category")

    def plot_combined_figures(self):
        words_per_category = self.df["category"].value_counts().sort_index()
        fig, axes = plt.subplots(2, 2, figsize=(16, 16))

        self._plot_words_per_category_ax(axes[0,0], words_per_category)
        self._plot_difficulty_vs_frequency_ax(axes[0,1])
        self._plot_english_word_length_distribution_ax(axes[1,0])
        self._plot_heatmap(axes[1,1])

        plt.tight_layout()
        plt.savefig("combined-figures.png")
        print("Combined plot saved as 'combined-figures.png'")

if __name__ == "__main__":
    # Part 1
    analyzer = VocabularyAnalyzer("vocabulary.csv")
    analyzer.analyze_dataset()
    analyzer.analyze_statistics()
    analyzer.analyze_missing_data()
    # Part 2
    analyzer.analyze_categories()
    analyzer.analyze_difficulty_level()
    analyzer.analyze_correlations()
    # Part 3
    analyzer.plot_combined_figures()