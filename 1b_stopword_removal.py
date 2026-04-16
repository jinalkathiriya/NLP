# b_stopword_removal.py

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Take input from user
text = input("Enter a sentence:\n")

# Tokenize
words = word_tokenize(text)

# Load stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

print("\nOriginal Words:")
print(words)

print("\nAfter Stopword Removal:")
print(filtered_words)
