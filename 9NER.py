import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

# Download required packages (only first time)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Take input from user
text = input("Enter a sentence: ")

# Step 1: Tokenization
tokens = word_tokenize(text)

# Step 2: POS Tagging
pos_tags = pos_tag(tokens)

# Step 3: Named Entity Recognition
named_entities = ne_chunk(pos_tags)

print("\nNamed Entities:\n")
print(named_entities)

# Show structured entities
print("\nExtracted Entities:\n")

for subtree in named_entities:
    if hasattr(subtree, 'label'):
        entity = " ".join([token for token, pos in subtree.leaves()])
        print(f"{entity} --> {subtree.label()}")