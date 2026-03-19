import pandas as pd

# Load all cleaned datasets
ceas = pd.read_csv("clean_ceas_dataset.csv")
nazario = pd.read_csv("clean_nazario_dataset.csv")
nigerian = pd.read_csv("clean_nigerian_dataset.csv")
enron = pd.read_csv("clean_enron_dataset.csv")
ling = pd.read_csv("clean_ling_dataset.csv")
spamassassin = pd.read_csv("clean_spamassasin_dataset.csv")

# Keep only required columns
datasets = [ceas, nazario, nigerian, enron, ling, spamassassin]

for i in range(len(datasets)):
    datasets[i] = datasets[i][["text", "label"]]

# Merge all
final_df = pd.concat(datasets, ignore_index=True)

# Shuffle
final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save
final_df.to_csv("final_unified_dataset.csv", index=False)

print("All datasets merged successfully!\n")
print("Final distribution:")
print(final_df["label"].value_counts())
print("\nTotal rows:", len(final_df))
