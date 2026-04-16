import nltk
from nltk.tokenize import word_tokenize

# Download required models
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Take input
text = input("Enter a sentence: ")

# Tokenize
tokens = word_tokenize(text)

# Statistical POS tagging
tagged = nltk.pos_tag(tokens)

print("\nStatistical POS Tagging:")
print(tagged)