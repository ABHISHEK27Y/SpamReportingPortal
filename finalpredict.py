import joblib
import sys

# Load trained model and vectorizer
model = joblib.load("final_model.pkl")
vectorizer = joblib.load("final_vectorizer.pkl")

print("=" * 60)
print(" UNIFIED FRAUD DETECTION SYSTEM ")
print("=" * 60)
print("Paste suspicious message below.")
print("Type END (in new line) to finish input.")
print("Type EXIT to quit.\n")

while True:
    print("\nEnter suspicious message:")
    
    lines = []
    while True:
        line = input()
        
        if line.strip().upper() == "EXIT":
            print("Exiting...")
            sys.exit()
        
        if line.strip().upper() == "END":
            break
        
        lines.append(line)
    
    message = "\n".join(lines).strip()
    
    if not message:
        print("⚠️ No input provided.")
        continue

    # Transform input
    message_tfidf = vectorizer.transform([message])
    
    # Predict
    prediction = model.predict(message_tfidf)[0]
    probability = model.predict_proba(message_tfidf)[0]

    fraud_prob = probability[1]
    legit_prob = probability[0]

    print("\n" + "-" * 50)

    if prediction == 1:
        print("🚨 Prediction: FRAUD / SPAM")
        print(f"Fraud Probability: {fraud_prob:.4f}")
        print(f"Legitimate Probability: {legit_prob:.4f}")
    else:
        print("✅ Prediction: LEGITIMATE")
        print(f"Legitimate Probability: {legit_prob:.4f}")
        print(f"Fraud Probability: {fraud_prob:.4f}")

    print("-" * 50)
