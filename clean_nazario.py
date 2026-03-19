import pandas as pd

# Load Nazario dataset
df = pd.read_csv("dataset/Nazario.csv")

# Combine subject + body
df['text'] = df['subject'].fillna('') + " " + df['body'].fillna('')

# Convert label (1 = Fraud, 0 = Not_Fraud)
df['label'] = df['label'].map({
    1: "Fraud",
    0: "Not_Fraud"
})

# Keep only needed columns
df = df[['text', 'label']]

# Remove empty rows
df = df.dropna()

# Save cleaned file
df.to_csv("clean_nazario_dataset.csv", index=False)

print("Nazario dataset cleaned successfully!")
print(df['label'].value_counts())
