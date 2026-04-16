import nltk
from nltk.corpus import wordnet

# Download WordNet (first time only)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Take input from user
word = input("Enter a word: ")

print("\nHypernyms of", word, ":")

for syn in wordnet.synsets(word):
    for hyper in syn.hypernyms():
        print(hyper.name(), "->", hyper.definition())