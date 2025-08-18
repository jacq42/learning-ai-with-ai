import pandas as pd
from numpy.f2py.crackfortran import analyzeargs

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

    def analyze_difficulty_level(self):
        print("\n📋 Difficulty Level Distribution:")
        difficulty_level_groups = self.df.groupby("difficulty")
        print(f"Total difficulty levels: {difficulty_level_groups.ngroups}")
        print(f"Words by difficulty level: {dict(difficulty_level_groups.size())}")
        print(f"Average frequency by difficulty level: {dict(difficulty_level_groups['frequency_rank'].mean())}")

if __name__ == "__main__":
    # Part 1
    analyzer = VocabularyAnalyzer("vocabulary.csv")
    analyzer.analyze_dataset()
    analyzer.analyze_statistics()
    analyzer.analyze_missing_data()
    # Part 2
    analyzer.analyze_categories()
    analyzer.analyze_difficulty_level()