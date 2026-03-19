import joblib
import os
import numpy as np

class MLEngine:
    def __init__(self, model_path="final_model.pkl", vectorizer_path="final_vectorizer.pkl"):
        # Ensure we are loading from the correct directory (current working directory usually)
        if not os.path.exists(model_path):
             raise FileNotFoundError(f"Model file not found at {model_path}")
        if not os.path.exists(vectorizer_path):
             raise FileNotFoundError(f"Vectorizer file not found at {vectorizer_path}")

        print("Loading models...")
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
        print("Models loaded successfully.")

    def predict(self, message):
        try:
            message_tfidf = self.vectorizer.transform([message])
            prediction = self.model.predict(message_tfidf)[0]
            probability = self.model.predict_proba(message_tfidf)[0]
            
            return {
                "prediction": int(prediction),
                "fraud_probability": float(probability[1]),
                "legit_probability": float(probability[0])
            }
        except Exception as e:
            print(f"Error during prediction: {e}")
            raise

# Initialize global instance
# We delay initialization until used or explicitly called to avoid import side effects if needed, 
# but for this simple app, instantiating here is fine if run from the main dir.
try:
    ml_engine = MLEngine()
except Exception as e:
    print(f"Failed to initialize MLEngine: {e}")
    ml_engine = None
