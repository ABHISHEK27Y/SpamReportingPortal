import pandas as pd
import random

base_phrases = [
    "Your bank account is suspended verify immediately",
    "Send money urgently or your account will be blocked",
    "Your UPI KYC expired update now",
    "Click link to avoid account deactivation",
    "Confirm OTP to secure your account",
    "Job offer processing fee required",
    "Pay registration fee to confirm job",
    "Your parcel delivery failed pay shipping fee",
    "Refund pending click to claim",
    "Account under verification send details now"
]

variations = [
    "immediately",
    "within 24 hours",
    "to avoid suspension",
    "to prevent blocking",
    "urgent action required",
    "failure to comply will result in closure"
]

generated = []

for _ in range(250):   # generate 250 fraud examples
    phrase = random.choice(base_phrases)
    extra = random.choice(variations)
    full_text = phrase + " " + extra
    generated.append([full_text, "Fraud"])

df = pd.DataFrame(generated, columns=["text", "label"])

df.to_csv("generated_modern_fraud.csv", index=False)

print("Generated modern fraud samples!")
