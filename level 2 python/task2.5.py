from collections import Counter
import re

def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        word_counts = Counter(words)
        sorted_word_counts = dict(sorted(word_counts.items()))
        return sorted_word_counts

filename = input("Enter the filename: ")
word_counts = count_words_in_file(filename)

for word, count in word_counts.items():
    print(f"{word}: {count}")
