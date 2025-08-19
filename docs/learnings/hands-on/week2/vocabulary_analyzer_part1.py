from vocabulary_analyzer_base import VocabularyAnalyzerBase

class VocabularyAnalyzerPart1(VocabularyAnalyzerBase):
    def __init__(self, csv_path):
        super().__init__(csv_path)

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
