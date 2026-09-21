import pandas as pd
import joblib

from pathlib import Path


# ==========================================
# FILE PATH
# ==========================================

MODEL_FILE = Path("models/ransomware_model.pkl")
TEST_FILE = Path("dataset/processed/test_data.csv")


# ==========================================
# LOAD MODEL
# ==========================================

print("Loading trained model...")

model = joblib.load(MODEL_FILE)

print("Model loaded successfully.")


# ==========================================
# LOAD TEST DATA
# ==========================================

df = pd.read_csv(TEST_FILE)

TARGET_COLUMN = "Benign"

X = df.drop(columns=[TARGET_COLUMN])

# Keep only numeric features
X = X.select_dtypes(include=["number"])


# ==========================================
# SELECT ONE SAMPLE
# ==========================================

sample = X.iloc[[0]]


# ==========================================
# MAKE PREDICTION
# ==========================================

prediction = model.predict(sample)[0]

probability = model.predict_proba(sample)[0]


# ==========================================
# DISPLAY RESULT
# ==========================================

print("\n================================")
print("RANSOMWARE DETECTION")
print("================================")

print("Prediction value:", prediction)

print("\nPrediction probabilities:")
print(probability)

if prediction == 1:
    print("\nResult: BENIGN")
else:
    print("\nResult: MALICIOUS")

print("\n================================")