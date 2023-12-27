# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Example data (replace this with your actual data)
data = {
    'job_description': ['Software Engineer with expertise in Python and machine learning.',
                        'Data Scientist with experience in statistical modeling.',
                        'Web Developer proficient in HTML, CSS, and JavaScript.'],
    'resume': ['Experienced software engineer with 3 years of Python development.',
               'Data scientist specializing in predictive analytics.',
               'Full-stack web developer with front-end and back-end expertise.'],
    'match': [1, 1, 0]  # 1 indicates a match, 0 indicates no match
}

df = pd.DataFrame(data)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['job_description', 'resume']], df['match'], test_size=0.2, random_state=42)

# Feature extraction using TF-IDF
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train['job_description'] + ' ' + X_train['resume'])
X_test_tfidf = vectorizer.transform(X_test['job_description'] + ' ' + X_test['resume'])

# Train a machine learning model (Random Forest in this example)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train_tfidf, y_train)

# Predictions on the test set
y_pred = clf.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_report_result = classification_report(y_test, y_pred)

# Print the results
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:\n', classification_report_result)
