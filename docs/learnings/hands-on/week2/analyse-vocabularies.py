import pandas as pd

data_frame = pd.read_csv('vocabulary.csv')

print("📊 Dataset Overview:")
print(f"Shape: {data_frame.shape}")
print(f"Columns: {list(data_frame.columns)}")
print("\nFirst 5 rows:")
print(data_frame.head())

empty_categories = data_frame[data_frame['category'].isna() | (data_frame['category'] == '')]
print("Items with empty category:")
print(empty_categories)