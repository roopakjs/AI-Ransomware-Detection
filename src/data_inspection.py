import pandas as pd
from pathlib import Path

DATASET_PATH = Path("dataset/raw/data_file.csv")

print("Loading dataset...")

df = pd.read_csv(DATASET_PATH)

print("\n========== DATASET INFORMATION ==========")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATES ==========")
print(df.duplicated().sum())

print("\n========== DATASET INFO ==========")
print(df.info())