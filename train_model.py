import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("final_unified_dataset.csv")

# Check class distribution
print("\nClass Distribution:")
print(df['label'].value_counts())

print("\nClass Percentage:")
print(df['label'].value_counts(normalize=True) * 100)


# Separate features and labels
X = df['text']
y = df['label']

# Train-test split (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(
    stop_words='english',
    max_features=5000
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("TF-IDF transformation complete.")
print("Training shape:", X_train_tfidf.shape)
print("Testing shape:", X_test_tfidf.shape)


# Train Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Predictions
y_pred = model.predict(X_test_tfidf)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel trained successfully!")
print("Accuracy:", accuracy)

# Detailed Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ===============================
# Probability-Based Risk Scoring
# ===============================

def predict_risk(text):
    # Convert text to TF-IDF
    text_tfidf = vectorizer.transform([text])

    # Get probability scores
    probs = model.predict_proba(text_tfidf)[0]

    # Find index of Fraud class
    fraud_index = list(model.classes_).index('Fraud')
    fraud_prob = probs[fraud_index]

    # Risk mapping
    if fraud_prob >= 0.7:
        risk = "High"
    elif fraud_prob >= 0.4:
        risk = "Medium"
    else:
        risk = "Low"

    return fraud_prob, risk


test_samples = [
    "Congratulations! You have won a free iPhone. Click now!",
    "Hey bro, are we meeting tomorrow at 5?",
    "Urgent! Your account is suspended. Verify immediately."
]

for text in test_samples:
    prob, risk = predict_risk(text)
    print("\nText:", text)
    print("Fraud Probability:", round(prob, 3))
    print("Risk Level:", risk)

import pickle

# Save model
with open("fraud_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("\nModel and vectorizer saved successfully!")
