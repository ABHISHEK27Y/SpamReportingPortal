import pandas as pd

# Load dataset
df = pd.read_csv("dataset/SpamAssasin.csv", encoding="latin-1")


print("Original shape:", df.shape)

# Combine subject + body
df['text'] = df['subject'].fillna('') + " " + df['body'].fillna('')

# Convert label
df['label'] = df['label'].astype(str)

df['label'] = df['label'].map({
    '1': 'Fraud',
    '0': 'Not_Fraud'
})

# Remove rows with invalid labels
df = df[df['label'].isin(['Fraud', 'Not_Fraud'])]

# Remove empty text rows
df = df[df['text'].notna()]
df = df[df['text'].str.strip() != ""]

# Keep only required columns
df = df[['text', 'label']]

df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("clean_spamassasin.csv", index=False)

print("\nSpamAssassin cleaned successfully!")
print(df['label'].value_counts())
print("Total rows:", len(df))
