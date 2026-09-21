import pandas as pd
import joblib
import json

from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# ==========================================
# FILE PATHS
# ==========================================

DATA_FILE = Path("dataset/processed/processed_data.csv")
MODEL_FILE = Path("models/ransomware_model.pkl")
FEATURE_FILE = Path("models/feature_names.json")

# ==========================================
# LOAD PROCESSED DATA
# ==========================================

print("Loading processed dataset...")

df = pd.read_csv(DATA_FILE)

print("Dataset shape:", df.shape)


# ==========================================
# SEPARATE FEATURES AND TARGET
# ==========================================

TARGET_COLUMN = "Benign"

if TARGET_COLUMN not in df.columns:
    raise ValueError(
        f"Target column '{TARGET_COLUMN}' was not found in the dataset."
    )

X = df.drop(columns=[TARGET_COLUMN])
y = df[TARGET_COLUMN]

print("\nFeatures:", X.shape)
print("Target:", y.shape)

print("\nTarget distribution:")
print(y.value_counts())


# ==========================================
# KEEP NUMERIC FEATURES ONLY
# ==========================================

X = X.select_dtypes(include=["number"])

print("\nNumeric features:", X.shape[1])
# Save the exact feature names and order
feature_names = X.columns.tolist()

FEATURE_FILE.parent.mkdir(parents=True, exist_ok=True)

with open(FEATURE_FILE, "w") as file:
    json.dump(feature_names, file, indent=4)

print("\nFeature names saved to:")
print(FEATURE_FILE)

# ==========================================
# TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])


# ==========================================
# RANDOM FOREST MODEL
# ==========================================

print("\nTraining Random Forest...")

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("Training completed!")


# ==========================================
# SAVE MODEL
# ==========================================

MODEL_FILE.parent.mkdir(parents=True, exist_ok=True)

joblib.dump(model, MODEL_FILE)

print("\nModel saved successfully:")
print(MODEL_FILE)


# ==========================================
# SAVE TEST DATA FOR EVALUATION
# ==========================================

test_data = X_test.copy()
test_data[TARGET_COLUMN] = y_test

test_data.to_csv(
    "dataset/processed/test_data.csv",
    index=False
)

print("Test data saved successfully.")

print("\n================================")
print("MODEL TRAINING COMPLETE")
print("================================")