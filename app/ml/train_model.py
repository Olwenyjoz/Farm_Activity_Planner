"""
=========================================================
Module: train_model.py

Purpose:
    Train the Crop Recommendation Machine Learning Model.

Responsibilities:
    - Load the crop training dataset.
    - Encode categorical features.
    - Split the dataset into training and testing sets.
    - Train a Random Forest Classifier.
    - Evaluate model performance.
    - Save the trained model and encoders.


=========================================================
"""

from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


# =====================================================
# PROJECT PATHS
# =====================================================

BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = (
    BASE_DIR /
    "dataset" /
    "crop_dataset.csv"
)

MODEL_PATH = (
    BASE_DIR /
    "crop_model.pkl"
)

SOIL_ENCODER_PATH = (
    BASE_DIR /
    "soil_encoder.pkl"
)

SEASON_ENCODER_PATH = (
    BASE_DIR /
    "season_encoder.pkl"
)

CROP_ENCODER_PATH = (
    BASE_DIR /
    "crop_encoder.pkl"
)


# =====================================================
# LOAD DATASET
# =====================================================

print("=" * 60)
print("Loading crop dataset...")
print("=" * 60)

dataset = pd.read_csv(
    DATASET_PATH
)

print(
    f"Dataset loaded successfully "
    f"({len(dataset)} records)"
)


# =====================================================
# ENCODE CATEGORICAL FEATURES
# =====================================================

print("\nEncoding categorical features...")

soil_encoder = LabelEncoder()

season_encoder = LabelEncoder()

crop_encoder = LabelEncoder()

dataset["soil_type"] = soil_encoder.fit_transform(
    dataset["soil_type"]
)

dataset["season"] = season_encoder.fit_transform(
    dataset["season"]
)

dataset["recommended_crop"] = crop_encoder.fit_transform(
    dataset["recommended_crop"]
)

print("Encoding completed successfully.")


# =====================================================
# PREPARE FEATURES
# =====================================================

print("\nPreparing training features...")

X = dataset[
    [
        "temperature",
        "humidity",
        "rainfall",
        "farm_size",
        "soil_type",
        "season"
    ]
]

y = dataset[
    "recommended_crop"
]

print("Features prepared successfully.")


# =====================================================
# SPLIT DATASET
# =====================================================

print("\nSplitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    shuffle=True
)

print(
    f"Training records : {len(X_train)}"
)

print(
    f"Testing records  : {len(X_test)}"
)


# =====================================================
# TRAIN MACHINE LEARNING MODEL
# =====================================================

print("\nTraining Random Forest Classifier...")

model = RandomForestClassifier(

    n_estimators=200,

    random_state=42

)

model.fit(

    X_train,

    y_train
)

print("Model training completed.")


# =====================================================
# EVALUATE MODEL
# =====================================================

print("\nEvaluating model...")

predictions = model.predict(

    X_test
)

accuracy = accuracy_score(

    y_test,

    predictions
)

print(
    f"Model Accuracy : {accuracy:.2%}"
)


# =====================================================
# SAVE TRAINED MODEL
# =====================================================

print("\nSaving trained model...")

joblib.dump(

    model,

    MODEL_PATH
)

joblib.dump(

    soil_encoder,

    SOIL_ENCODER_PATH
)

joblib.dump(

    season_encoder,

    SEASON_ENCODER_PATH
)

joblib.dump(

    crop_encoder,

    CROP_ENCODER_PATH
)

print("Machine Learning model saved successfully.")

print("Encoders saved successfully.")


# =====================================================
# TRAINING SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("TRAINING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"Dataset           : {DATASET_PATH}")

print(f"Model             : {MODEL_PATH}")

print(f"Soil Encoder      : {SOIL_ENCODER_PATH}")

print(f"Season Encoder    : {SEASON_ENCODER_PATH}")

print(f"Crop Encoder      : {CROP_ENCODER_PATH}")

print(f"Accuracy          : {accuracy:.2%}")

print("=" * 60)