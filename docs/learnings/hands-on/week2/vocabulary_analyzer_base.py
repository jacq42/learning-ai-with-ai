import pandas as pd

class VocabularyAnalyzerBase:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)