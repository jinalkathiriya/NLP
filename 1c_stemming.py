# c_stemming.py

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Download required resource (run once)
nltk.download('punkt')

# Take input from user
text = input("Enter words or sentence:\n")

# Tokenize
words = word_tokenize(text)

# Initialize Stemmer
ps = PorterStemmer()

# Apply stemming
stemmed_words = [ps.stem(word) for word in words]

print("\nOriginal Words:")
print(words)

print("\nStemmed Words:")
print(stemmed_words)
