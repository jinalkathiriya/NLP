import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter

# Download tokenizer (only first time)
nltk.download('punkt')

# Take input from user
text = input("Enter text: ")

# Tokenize
tokens = word_tokenize(text.lower())

# Create bigrams
bigrams = list(ngrams(tokens, 2))

# Count unigrams and bigrams
unigram_counts = Counter(tokens)
bigram_counts = Counter(bigrams)

# Vocabulary
vocab = set(tokens)
V = len(vocab)

print("\nVocabulary Size:", V)

# --- Show Vocabulary Words ---
print("\nVocabulary Words:")
for word in vocab:
    print(word)

# --- Show Bigram Counts ---
print("\n--- Bigram Counts ---")
for bigram, count in bigram_counts.items():
    print(f"{bigram} : {count}")

print("\n--- Bigram Probabilities (Laplace Smoothed) ---")

# Laplace Smoothing Formula:
# P(w2|w1) = (C(w1,w2) + 1) / (C(w1) + V)

for bigram in bigram_counts:
    w1, w2 = bigram
    probability = (bigram_counts[bigram] + 1) / (unigram_counts[w1] + V)
    print(f"P({w2}|{w1}) = {probability:.4f}")