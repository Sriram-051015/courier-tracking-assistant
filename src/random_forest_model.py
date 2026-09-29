import os
import joblib
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


# ============================================================
# 1. Load training and testing data
# ============================================================

X_train = pd.read_csv("data/processed/X_train.csv")
X_test = pd.read_csv("data/processed/X_test.csv")

y_train = pd.read_csv("data/processed/y_train.csv").squeeze()
y_test = pd.read_csv("data/processed/y_test.csv").squeeze()

print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# ============================================================
# 2. Convert categorical column to numeric
# ============================================================

X_train = pd.get_dummies(
    X_train,
    columns=["aoi_type"]
)

X_test = pd.get_dummies(
    X_test,
    columns=["aoi_type"]
)


# Make sure training and testing columns match
X_test = X_test.reindex(
    columns=X_train.columns,
    fill_value=0
)


# ============================================================
# 3. Create Random Forest model
# ============================================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)


# ============================================================
# 4. Train model
# ============================================================

print("\n===== TRAINING RANDOM FOREST =====")

model.fit(
    X_train,
    y_train
)

print("Training completed.")

import os

model_path = "models/eta_random_forest.pkl"

joblib.dump(model, model_path)

print("Model saved successfully:")
print(model_path)

print(
    "Model file size:",
    os.path.getsize(model_path),
    "bytes"
)
# ============================================================
# 5. Make predictions
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# 6. Evaluate model
# ============================================================

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)


# ============================================================
# 7. Display results
# ============================================================

print("\n===== RANDOM FOREST RESULTS =====")

print("MAE:", round(mae, 2), "minutes")

print("RMSE:", round(rmse, 2), "minutes")


# ============================================================
# 8. Compare with previous models
# ============================================================

print("\n===== MODEL COMPARISON =====")

print("Baseline MAE: 108.46 minutes")
print("Linear Regression MAE: 102.92 minutes")
print("Random Forest MAE:", round(mae, 2), "minutes")

print("\nBaseline RMSE: 147.31 minutes")
print("Linear Regression RMSE: 141.06 minutes")
print("Random Forest RMSE:", round(rmse, 2), "minutes")


if mae < 102.92:
    print("\nRandom Forest improved Linear Regression.")
else:
    print("\nRandom Forest did not improve Linear Regression.")