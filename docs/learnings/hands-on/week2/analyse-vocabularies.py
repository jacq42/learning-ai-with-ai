from vocabulary_analyzer_part1 import VocabularyAnalyzerPart1
from vocabulary_analyzer_part2 import VocabularyAnalyzerPart2
from vocabulary_analyzer_part3 import VocabularyAnalyzerPart3
from vocabulary_analyzer_part4 import VocabularyAnalyzerPart4

if __name__ == "__main__":
    loop = True
    while loop:
        choice = input("\nChoose the part to run (1, 2, 3, 4 or q): ").strip()
        csvFilePath = "vocabulary.csv"
        if choice == "1":
            analyzerP1 = VocabularyAnalyzerPart1(csvFilePath)
            analyzerP1.analyze_dataset()
            analyzerP1.analyze_statistics()
            analyzerP1.analyze_missing_data()
        elif choice == "2":
            analyzerP2 = VocabularyAnalyzerPart2(csvFilePath)
            analyzerP2.analyze_categories()
            analyzerP2.analyze_difficulty_level()
            analyzerP2.analyze_correlations()
        elif choice == "3":
            analyzerP3 = VocabularyAnalyzerPart3(csvFilePath)
            analyzerP3.plot_combined_figures()
        elif choice == "4":
            analyzerP4 = VocabularyAnalyzerPart4(csvFilePath)
            analyzerP4.perform_text_processing('en', ['th', 'sh', 'ful', 'ed'])
            analyzerP4.perform_text_processing('de', ['lich', 'ig', 'dt'])
        elif choice.lower() == "q":
            print("Goodbye!")
            loop = False