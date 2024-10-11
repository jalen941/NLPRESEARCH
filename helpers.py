# helper.py
import pronouncing

class Helpers:
    def read_words_from_file(self, filename):
        """Read words from a specified text file."""
        with open(filename, 'r') as file:
            # Read the lines and strip whitespace
            words = [line.strip() for line in file.readlines()]
        return words

    def get_phonetic_representation(self, words):
        """Get phonetic representation for a list of words."""
        # Get phonetic representation for each word
        phonetic_data = [(word, pronouncing.phones_for_word(word)[0]) for word in words if pronouncing.phones_for_word(word)]
        return phonetic_data
