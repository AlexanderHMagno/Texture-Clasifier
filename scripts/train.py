import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load extracted features
df = pd.read_csv("data/features.csv")
X = df.iloc[:, 1:].values  # Features
y = df.iloc[:, 0].values  # Labels

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)

# Train RandomForest
rf_model = RandomForestClassifier(n_estimators=100)
rf_model.fit(X_train, y_train)

# Evaluate
print(f"SVM Accuracy: {accuracy_score(y_test, svm_model.predict(X_test)):.2f}")
print(f"RF Accuracy: {accuracy_score(y_test, rf_model.predict(X_test)):.2f}")

# Save models
joblib.dump(svm_model, "models/svm_model.pkl")
joblib.dump(rf_model, "models/rf_model.pkl")

print("✅ Models trained and saved!")
