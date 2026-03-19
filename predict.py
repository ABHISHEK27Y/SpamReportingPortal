import pickle

# Load saved model
with open("fraud_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load saved vectorizer
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def predict_risk(text):
    # Convert text to TF-IDF
    text_tfidf = vectorizer.transform([text])

    # Get probability
    probs = model.predict_proba(text_tfidf)[0]

    # Get fraud probability
    fraud_index = list(model.classes_).index('Fraud')
    fraud_prob = probs[fraud_index]

    # Risk scoring
    if fraud_prob >= 0.7:
        risk = "High"
    elif fraud_prob >= 0.4:
        risk = "Medium"
    else:
        risk = "Low"

    return fraud_prob, risk


# ==============================
# Take User Input
# ==============================

while True:
    user_input = input("\nEnter message (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        break

    prob, risk = predict_risk(user_input)

    print("Fraud Probability:", round(prob, 3))
    print("Risk Level:", risk)
