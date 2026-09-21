import pandas as pd
import joblib
import json

from pathlib import Path

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ============================================================
# FILE PATHS
# ============================================================

TEST_DATA_FILE = Path("dataset/processed/test_data.csv")
MODEL_FILE = Path("models/ransomware_model.pkl")

RESULTS_DIR = Path("reports/results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

METRICS_FILE = RESULTS_DIR / "metrics.json"
REPORT_FILE = RESULTS_DIR / "evaluation_results.txt"


# ============================================================
# LOAD MODEL
# ============================================================

print("Loading model...")

model = joblib.load(MODEL_FILE)


# ============================================================
# LOAD TEST DATA
# ============================================================

print("Loading test data...")

df = pd.read_csv(TEST_DATA_FILE)


# ============================================================
# TARGET COLUMN
# ============================================================

TARGET_COLUMN = "Benign"


if TARGET_COLUMN not in df.columns:

    raise ValueError(
        f"Target column '{TARGET_COLUMN}' not found."
    )


# ============================================================
# PREPARE X AND Y
# ============================================================

y = df[TARGET_COLUMN]

X = df.drop(
    columns=[TARGET_COLUMN]
)


# Keep numeric features only

X = X.select_dtypes(
    include=["number"]
)


# ============================================================
# FEATURE ORDER
# ============================================================

FEATURE_FILE = Path(
    "models/feature_names.json"
)


if FEATURE_FILE.exists():

    with open(FEATURE_FILE, "r") as file:

        feature_names = json.load(file)

    X = X[feature_names]


# ============================================================
# PREDICTION
# ============================================================

print("Making predictions...")

y_pred = model.predict(X)


# ============================================================
# CALCULATE METRICS
# ============================================================

accuracy = accuracy_score(
    y,
    y_pred
)

precision = precision_score(
    y,
    y_pred,
    average="weighted",
    zero_division=0
)

recall = recall_score(
    y,
    y_pred,
    average="weighted",
    zero_division=0
)

f1 = f1_score(
    y,
    y_pred,
    average="weighted",
    zero_division=0
)


# ============================================================
# CONFUSION MATRIX
# ============================================================

cm = confusion_matrix(
    y,
    y_pred
)


# ============================================================
# CLASSIFICATION REPORT
# ============================================================

report = classification_report(
    y,
    y_pred,
    zero_division=0
)


# ============================================================
# SAVE METRICS AS JSON
# ============================================================

metrics = {

    "accuracy": float(accuracy),

    "precision": float(precision),

    "recall": float(recall),

    "f1_score": float(f1),

    "confusion_matrix": cm.tolist()

}


with open(
    METRICS_FILE,
    "w"
) as file:

    json.dump(
        metrics,
        file,
        indent=4
    )


# ============================================================
# SAVE TEXT REPORT
# ============================================================

with open(
    REPORT_FILE,
    "w"
) as file:

    file.write(
        "AI-BASED RANSOMWARE DETECTION\n"
    )

    file.write(
        "MODEL EVALUATION RESULTS\n"
    )

    file.write(
        "====================================\n\n"
    )

    file.write(
        f"Accuracy: {accuracy:.6f}\n"
    )

    file.write(
        f"Precision: {precision:.6f}\n"
    )

    file.write(
        f"Recall: {recall:.6f}\n"
    )

    file.write(
        f"F1 Score: {f1:.6f}\n\n"
    )

    file.write(
        "Classification Report\n"
    )

    file.write(
        "====================================\n"
    )

    file.write(
        report
    )

    file.write(
        "\n\nConfusion Matrix\n"
    )

    file.write(
        "====================================\n"
    )

    file.write(
        str(cm)
    )


# ============================================================
# DISPLAY RESULTS
# ============================================================

print("\n====================================")
print("MODEL EVALUATION COMPLETE")
print("====================================")

print(
    f"Accuracy  : {accuracy:.4f}"
)

print(
    f"Precision : {precision:.4f}"
)

print(
    f"Recall    : {recall:.4f}"
)

print(
    f"F1 Score  : {f1:.4f}"
)

print("\nConfusion Matrix:")
print(cm)

print(
    f"\nMetrics saved to: {METRICS_FILE}"
)

print(
    f"Report saved to: {REPORT_FILE}"
)