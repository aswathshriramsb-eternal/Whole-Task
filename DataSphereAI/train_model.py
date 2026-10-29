"""
train_model.py
Trains the Decision Tree Classifier for Project 04 and exports the artifact for Project 05.
Uses a clean Scikit-learn Pipeline to guarantee consistent preprocessing without data leakage.
"""

import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "titanic.csv")
MODEL_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, "titanic_model.joblib")

# Load Titanic dataset
df = pd.read_csv(DATA_PATH)

# Features & Target
FEATURES = ["pclass", "sex", "age", "fare"]
TARGET = "survived"

X = df[FEATURES]
y = df[TARGET]

# Split 80/20 train/test with fixed seed and stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

# Preprocessing:
# Numeric: pclass, age, fare -> median imputation
# Categorical: sex -> one-hot encoding
numeric_features = ["pclass", "age", "fare"]
categorical_features = ["sex"]

numeric_transformer = SimpleImputer(strategy="median")
categorical_transformer = OneHotEncoder(drop="first", handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

# Optimal Decision Tree Pipeline (max_depth=3 to prevent overfitting)
model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", DecisionTreeClassifier(max_depth=3, random_state=42)),
    ]
)

# Train model
model_pipeline.fit(X_train, y_train)

# Evaluate on held-out test set
y_pred = model_pipeline.predict(X_test)
y_pred_proba = model_pipeline.predict_proba(X_test)[:, 1]

acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
baseline_acc = (y_test == 0).mean()

print("=======================================================")
print(" PROJECT 04: MODEL TRAINING & EVALUATION REPORT")
print("=======================================================")
print(f"Training Samples:   {len(X_train)}")
print(f"Test Samples:       {len(X_test)}")
print(f"Baseline Accuracy:  {baseline_acc * 100:.2f}% (Majority Class = 0: Died)")
print(f"Test Accuracy:      {acc * 100:.2f}%")
print(f"Test Precision:     {prec * 100:.2f}%")
print(f"Test Recall:        {rec * 100:.2f}%")
print(f"Test F1-Score:      {f1 * 100:.2f}%")
print(f"Confusion Matrix:\n{cm}")

# Save model artifact and metadata
metadata = {
    "features": FEATURES,
    "target": TARGET,
    "test_accuracy": acc,
    "test_precision": prec,
    "test_recall": rec,
    "test_f1": f1,
    "confusion_matrix": cm.tolist(),
    "baseline_accuracy": baseline_acc,
    "train_size": len(X_train),
    "test_size": len(X_test)
}

artifact = {
    "pipeline": model_pipeline,
    "metadata": metadata
}

joblib.dump(artifact, MODEL_PATH)
print(f"\nSaved trained model bundle to {MODEL_PATH}")
