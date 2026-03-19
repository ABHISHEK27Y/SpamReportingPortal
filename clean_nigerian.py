import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Nigerian_Fraud.csv")

# Combine subject + body
df['text'] = df['subject'].fillna('') + " " + df['body'].fillna('')

# Convert label column
df['label'] = df['label'].map({
    1: "Fraud",
    0: "Not_Fraud"
})

# Keep only needed columns
df = df[['text', 'label']]

# Drop empty rows
df = df.dropna()

# Save cleaned dataset
df.to_csv("clean_nigerian_dataset.csv", index=False)

print("Nigerian dataset cleaned successfully!")
print(df['label'].value_counts())
