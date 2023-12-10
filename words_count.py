from collections import Counter
import string

def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the file content
            content = file.read().lower()

            # Remove punctuation
            content = content.translate(str.maketrans('', '', string.punctuation))

            # Split the content into words
            words = content.split()

            # Count the occurrences of each word
            word_counts = Counter(words)

            return word_counts

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

#Actual path to your text file
file_path = r'C:\Users\BANA NKANDU\Documents\cse111\wordcounttext.txt'

# Count words
word_counts = count_words(file_path)

if word_counts:
    # Print the word counts
    for word, count in word_counts.items():
        print(f"{word}: {count}")
