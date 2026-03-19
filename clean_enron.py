import pandas as pd
import re

# Load dataset
df = pd.read_csv("dataset/Enron.csv")

# Combine subject + body
df["text"] = df["subject"].fillna("") + " " + df["body"].fillna("")

# Text cleaning function
def clean_text(text):
    text = str(text).lower()

    # Remove email header noise
    text = re.sub(r"forwarded by.*", "", text)
    text = re.sub(r"from:.*", "", text)
    text = re.sub(r"to:.*", "", text)
    text = re.sub(r"cc:.*", "", text)

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove excessive punctuation
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()

# Apply cleaning
df["text"] = df["text"].apply(clean_text)

# Remove very short emails (mostly useless)
df = df[df["text"].str.len() > 30]

# Keep only text
df_clean = df[["text"]].copy()
df_clean["label"] = "Not_Fraud"

# 🔥 Downsample to prevent imbalance
sample_size = 7000

if len(df_clean) > sample_size:
    df_clean = df_clean.sample(n=sample_size, random_state=42)

# Save cleaned dataset
df_clean.to_csv("clean_enron_dataset.csv", index=False)

print("Enron dataset cleaned and downsampled successfully!")
print(df_clean["label"].value_counts())
print("Total rows:", len(df_clean))
