import nltk
import random
from nltk.corpus import movie_reviews
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Download dataset
nltk.download('movie_reviews')

# Load dataset
documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        review = movie_reviews.raw(fileid)
        documents.append((review, category))

# Shuffle dataset
random.shuffle(documents)

# Separate reviews and labels
reviews = [doc[0] for doc in documents]
labels = [doc[1] for doc in documents]

# Convert text into numerical features
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(reviews)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict accuracy
predictions = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, predictions))

# User input for prediction
user_input = input("\nEnter a sentence to analyze sentiment: ")

user_vector = vectorizer.transform([user_input])

prediction = model.predict(user_vector)

print("\nSentiment:", prediction[0])