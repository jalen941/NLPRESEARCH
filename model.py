from helpers import Helpers
help =  Helpers()

# Read words from the file
words = help.read_words_from_file('words_list.txt')

# Get phonetic representations
phonetic_data = help.get_phonetic_representation(words)

# Print the results
print(phonetic_data)


def create_sequences(phonetic_data):
    sequences = []
    for word, phonetic in phonetic_data:
        phonemes = phonetic.split()
        for i in range(1, len(phonemes)):
            input_seq = phonemes[:i]   # e.g., ['HH', 'AH0']
            target_phoneme = phonemes[i]  # e.g., 'L'
            sequences.append((input_seq, target_phoneme))
    return sequences

# Example result:
# [(['HH'], 'AH0'), (['HH', 'AH0'], 'L'), (['HH', 'AH0', 'L'], 'OW1'), ...]
sequences = create_sequences(phonetic_data)

print(sequences)


