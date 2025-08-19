from vocabulary_analyzer_base import VocabularyAnalyzerBase

import pandas as pd

class VocabularyAnalyzerPart4(VocabularyAnalyzerBase):
    def __init__(self, csv_path):
        super().__init__(csv_path)

    def _english_to_lowercase(self):
        english_words = self.df['english'].str.lower().sort_values()
        print(f"\nConverted and sorted all to lowercase:\n {english_words.values}")
        return english_words

    def _german_to_lowercase(self):
        german_words = self.df['german'].str.lower().sort_values()
        print(f"\nConverted and sorted all to lowercase:\n {german_words.values}")
        return german_words

    def perform_text_processing(self, language, letter_patterns):
        if language == 'de':
            lowercase_words = self._german_to_lowercase()
        else:
            lowercase_words = self._english_to_lowercase()
        all_chars = ''.join(lowercase_words)
        alpha_chars = ''.join(c for c in all_chars if c.isalnum())
        char_freq = pd.Series(list(alpha_chars)).value_counts()
        print(f"\nCharacter frequency:\n{char_freq.sort_values(ascending=False)[:4]}")

        for pattern in letter_patterns:
            matching_words = lowercase_words[lowercase_words.str.contains(pattern, na=False)]
            print(f"\n- Pattern '{pattern}': {len(matching_words)} matches")
            print(f"  Sample: {matching_words[:5].values}")