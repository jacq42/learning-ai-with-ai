from vocabulary_analyzer_part1 import VocabularyAnalyzerPart1
from vocabulary_analyzer_part2 import VocabularyAnalyzerPart2
from vocabulary_analyzer_part3 import VocabularyAnalyzerPart3

if __name__ == "__main__":
    # Part 1
    analyzerP1 = VocabularyAnalyzerPart1("vocabulary.csv")
    analyzerP1.analyze_dataset()
    analyzerP1.analyze_statistics()
    analyzerP1.analyze_missing_data()
    # Part 2
    analyzerP2 = VocabularyAnalyzerPart2("vocabulary.csv")
    analyzerP2.analyze_categories()
    analyzerP2.analyze_difficulty_level()
    analyzerP2.analyze_correlations()
    # Part 3
    analyzerP3 = VocabularyAnalyzerPart3("vocabulary.csv")
    analyzerP3.plot_combined_figures()