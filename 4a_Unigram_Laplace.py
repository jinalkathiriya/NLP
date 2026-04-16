import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Download tokenizer (only first time)
nltk.download('punkt')

# Take input from user
text = input("Enter text: ")

# Tokenize
tokens = word_tokenize(text.lower())

# Count words
unigram_counts = Counter(tokens)
total_words = len(tokens)

# Vocabulary
vocab = set(tokens)
V = len(vocab)

print("\nVocabulary Size:", V)

# --- Show Vocabulary Words ---
print("\nVocabulary Words:")
for word in vocab:
    print(word)

# --- Show Unigram Counts ---
print("\n--- Unigram Counts ---")
for word, count in unigram_counts.items():
    print(f"{word} : {count}")

print("\n--- Unigram Probabilities (Laplace Smoothed) ---")

# Laplace Smoothing Formula:
# P(w) = (C(w) + 1) / (N + V)

for word in vocab:
    probability = (unigram_counts[word] + 1) / (total_words + V)
    print(f"P({word}) = {probability:.4f}")