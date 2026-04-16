import nltk
from nltk.metrics import edit_distance

# Take input from user
string1 = input("\nEnter first string: ")
string2 = input("\nEnter second string: ")

# Compute Levenshtein Distance
distance = edit_distance(string1, string2)

print("\nMinimum Edit Distance (Levenshtein Distance):", distance)