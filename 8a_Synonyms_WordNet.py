import nltk
from nltk.corpus import wordnet as wn

# Download WordNet dataset
nltk.download('wordnet')
nltk.download('omw-1.4')

# User input
word = input("Enter a word: ")

# Get synsets
synsets = wn.synsets(word)

if not synsets:
    print("Word not found in WordNet.")
else:
    syn = synsets[0]   # take first meaning

    print("\nWord Entered:", word)
    print("\nSynset:", syn.name())
    print("Definition:", syn.definition())

    # Synonyms
    print("\nSynonyms:")
    synonyms = set()
    for lemma in syn.lemmas():
        synonyms.add(lemma.name())

    for s in synonyms:
        print("-", s)

    # Hypernyms
    print("\nHypernyms:")
    for hyper in syn.hypernyms():
        print("-", hyper.name(), ":", hyper.definition())