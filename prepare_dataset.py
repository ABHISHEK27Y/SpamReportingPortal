import pandas as pd

# Load dataset (change path if needed)
df = pd.read_csv("dataset/spam.csv", encoding="latin-1")

# Keep only label and text columns
df = df[['v1', 'v2']]

# Rename columns
df.columns = ['label', 'text']

# Convert labels
df['label'] = df['label'].map({
    'spam': 'Fraud',
    'ham': 'Not_Fraud'
})

# Remove duplicates
df = df.drop_duplicates()

# Remove empty rows
df = df.dropna()

# Save cleaned dataset
df.to_csv("unified_fraud_dataset.csv", index=False)

print("Dataset cleaned successfully!")
print(df.head())
print("Total rows:", len(df))
