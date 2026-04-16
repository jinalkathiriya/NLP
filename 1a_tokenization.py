# a_tokenization.py

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required resource (run once)
nltk.download('punkt')
nltk.download('punkt_tab')

# Take input from user
text = input("Enter a sentence or paragraph:\n")

# Sentence Tokenization
sentences = sent_tokenize(text)
print("\nSentence Tokenization:")
print(sentences)

# Word Tokenization
words = word_tokenize(text)
print("\nWord Tokenization:")
print(words)
