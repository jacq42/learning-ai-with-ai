from vocabulary_analyzer_base import VocabularyAnalyzerBase
import matplotlib.pyplot as plt
import seaborn as sns

class VocabularyAnalyzerPart3(VocabularyAnalyzerBase):
    def __init__(self, csv_path):
        super().__init__(csv_path)

    @staticmethod
    def _plot_words_per_category_ax(ax, words_per_category):
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