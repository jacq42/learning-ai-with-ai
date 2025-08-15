import pandas as pd

def import_vocabulary():
    df = pd.read_csv('vocabulary.csv')

    print("📊 Dataset Overview:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    dtype_dict = {col: str(dtype) for col, dtype in df.dtypes.items()}
    print(f"Datatypes:\n{dtype_dict}")
    print("\nFirst 5 rows:")
    print(df.head())
    return df

def analyze_categories(df):
    empty_categories = df[df['category'].isna() | (df['category'] == '')]
    print(f"\nItems with empty category ({len(empty_categories)}):")
    print(empty_categories)

def analyze_statistics(df):
    aggregation = df.agg(
        {
            "difficulty": ["min", "max", "median", "mean"],
            "frequency_rank": ["min", "max", "median", "mean"],
        }
    )
    print("\n📊 Aggregated Statistics:\n")
    print(aggregation)

def print_statistics(df):
    print("\n📈 Vocabulary Statistics:")
    analyze_categories(df)
    analyze_statistics(df)

data = import_vocabulary()
print_statistics(data)