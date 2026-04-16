import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define grammar
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP

Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'mouse'
V -> 'chased' | 'saw' | 'ate'
""")

# Create parser
parser = ChartParser(grammar)

# User input
sentence = input("\nEnter a sentence: ")
words = sentence.lower().split()
print("\nParse Tree Output:\n")

# Parse sentence
for tree in parser.parse(words):
    print(tree)
    tree.pretty_print()