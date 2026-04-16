import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import RegexpTagger

# Download tokenizer
nltk.download('punkt')

# Take input
text = input("Enter a sentence: ")

# Tokenize
tokens = word_tokenize(text)

# Define grammar rules
patterns = [
    (r'.*ing$', 'VBG'),     # words ending with ing → gerund
    (r'.*ed$', 'VBD'),      # words ending with ed → past tense
    (r'.*es$', 'VBZ'),      # verbs ending with es
    (r'.*ould$', 'MD'),     # modal verbs
    (r'.*\'s$', 'NN$'),     # possessive nouns
    (r'.*s$', 'NNS'),       # plural nouns
    (r'^-?[0-9]+$', 'CD'),  # numbers
    (r'.*', 'NN')           # default noun
]

# Create tagger
rule_tagger = RegexpTagger(patterns)

# Tag sentence
tagged = rule_tagger.tag(tokens)

print("\nRule-Based POS Tagging:")
print(tagged)