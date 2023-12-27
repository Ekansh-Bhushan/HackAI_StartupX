from sklearn.feature_extraction.text import TfidfVectorizer

# Sample documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# Create the TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(documents)

# Get feature names (terms)
feature_names = vectorizer.get_feature_names_out()

# Create a DataFrame for better visualization
import pandas as pd
df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

# Display the TF-IDF matrix
print(df)
