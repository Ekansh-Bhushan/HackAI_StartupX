import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import spacy

# Sample data (you should replace this with your actual dataset)
data = {
    'Job_Description': [
        "Software Engineer with experience in Python and Java",
        "Data Scientist with expertise in machine learning",
        "Marketing Specialist with strong social media skills",
    ],
    'Resume': [
        "Experienced software developer proficient in Python and Java programming.",
        "Data science enthusiast with hands-on experience in machine learning algorithms.",
        "Marketing professional with a focus on social media marketing strategies.",
    ],
    'Label': [1, 1, 0]  # 1 for relevant, 0 for not relevant
}

df = pd.DataFrame(data)

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

# Tokenize and lemmatize the text using spaCy
def preprocess_text(text):
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

# Preprocess job descriptions and resumes
df['Job_Description'] = df['Job_Description'].apply(preprocess_text)
df['Resume'] = df['Resume'].apply(preprocess_text)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Transform the text data into TF-IDF features
X = vectorizer.fit_transform(df['Job_Description'] + df['Resume'])
y = df['Label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Support Vector Machine (SVM) classifier
classifier = SVC(kernel="linear")
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
