import pandas as pd

# Load dataset
df = pd.read_csv("dataset/Ling.csv")

# Keep only needed columns
df = df[['subject', 'body', 'label']]

# Combine subject + body
df['text'] = df['subject'].fillna('') + " " + df['body'].fillna('')

# Keep only text + label
df = df[['text', 'label']]

# Rename label
df['label'] = df['label'].apply(lambda x: "Fraud" if x == 1 else "Not_Fraud")

# Remove empty rows
df = df[df['text'].str.strip() != ""]

# Save cleaned version
df.to_csv("clean_ling.csv", index=False)

print("Ling dataset cleaned successfully!")
print(df['label'].value_counts())
print("Total rows:", len(df))
