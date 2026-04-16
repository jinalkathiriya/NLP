import nltk
import numpy as np
from nltk.corpus import treebank
from collections import defaultdict, Counter

# Download required dataset
nltk.download('treebank')
nltk.download('punkt')

# Load tagged sentences
tagged_sentences = treebank.tagged_sents()

# Training data
train_data = tagged_sentences[:3000]

# Count occurrences
transition_counts = defaultdict(Counter)
emission_counts = defaultdict(Counter)
tag_counts = Counter()

for sentence in train_data:

    prev_tag = "<s>"

    for word, tag in sentence:

        tag_counts[tag] += 1
        transition_counts[prev_tag][tag] += 1
        emission_counts[tag][word] += 1

        prev_tag = tag


# Calculate probabilities
transition_probs = defaultdict(dict)
emission_probs = defaultdict(dict)

for prev_tag in transition_counts:
    total = sum(transition_counts[prev_tag].values())

    for tag in transition_counts[prev_tag]:
        transition_probs[prev_tag][tag] = transition_counts[prev_tag][tag] / total


for tag in emission_counts:
    total = sum(emission_counts[tag].values())

    for word in emission_counts[tag]:
        emission_probs[tag][word] = emission_counts[tag][word] / total


# Viterbi Algorithm
def viterbi(sentence, tags):

    V = [{}]
    path = {}

    # Initialization step
    for tag in tags:

        transition = transition_probs.get("<s>", {}).get(tag, 1e-6)
        emission = emission_probs.get(tag, {}).get(sentence[0], 1e-6)

        V[0][tag] = transition * emission
        path[tag] = [tag]

    # Recursion step
    for t in range(1, len(sentence)):

        V.append({})
        new_path = {}

        for curr_tag in tags:

            max_prob = -1
            best_prev = None

            for prev_tag in tags:

                transition = transition_probs.get(prev_tag, {}).get(curr_tag, 1e-6)
                emission = emission_probs.get(curr_tag, {}).get(sentence[t], 1e-6)

                prob = V[t-1][prev_tag] * transition * emission

                if prob > max_prob:
                    max_prob = prob
                    best_prev = prev_tag

            V[t][curr_tag] = max_prob
            new_path[curr_tag] = path[best_prev] + [curr_tag]

        path = new_path

    # Termination step
    max_prob = -1
    best_tag = None

    for tag in tags:
        if V[len(sentence)-1][tag] > max_prob:
            max_prob = V[len(sentence)-1][tag]
            best_tag = tag

    return list(zip(sentence, path[best_tag]))


# Get list of POS tags
tags = list(tag_counts.keys())


# Take sentence input from user
user_sentence = input("\nEnter a sentence: ")

sentence = user_sentence.split()

# Run Viterbi algorithm
result = viterbi(sentence, tags)


# Print result
print("\nPOS Tagging Result:\n")

for word, tag in result:
    print(word, "->", tag)