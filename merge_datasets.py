import pandas as pd

original = pd.read_csv("unified_fraud_dataset.csv")
modern = pd.read_csv("generated_modern_fraud.csv")

combined = pd.concat([original, modern])

combined = combined.drop_duplicates()

combined.to_csv("final_unified_dataset.csv", index=False)

print("Datasets merged successfully!")
print(combined['label'].value_counts())
