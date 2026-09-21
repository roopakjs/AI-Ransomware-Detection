import pandas as pd
from pathlib import Path


# ==============================
# FILE PATHS
# ==============================

INPUT_FILE = Path("dataset/raw/data_file.csv")
OUTPUT_FILE = Path("dataset/processed/processed_data.csv")


# ==============================
# LOAD DATASET
# ==============================

print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print("Original shape:", df.shape)


# ==============================
# REMOVE DUPLICATES
# ==============================

duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)


# ==============================
# HANDLE MISSING VALUES
# ==============================

print("\nChecking missing values...")

missing_values = df.isnull().sum()

print(missing_values[missing_values > 0])

# Fill numeric missing values with median
numeric_columns = df.select_dtypes(include=["number"]).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())


# ==============================
# REMOVE TEXT IDENTIFIER COLUMNS
# ==============================

columns_to_remove = []

for column in ["FileName", "md5Hash"]:
    if column in df.columns:
        columns_to_remove.append(column)

if columns_to_remove:
    print("\nRemoving identifier columns:", columns_to_remove)
    df = df.drop(columns=columns_to_remove)


# ==============================
# SAVE PROCESSED DATASET
# ==============================

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

print("\n==============================")
print("PREPROCESSING COMPLETE")
print("==============================")

print("Final shape:", df.shape)
print("Saved to:", OUTPUT_FILE)