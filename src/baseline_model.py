import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

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
# 2. Create baseline prediction
# ============================================================

# Use the average delivery duration from the training data
baseline_prediction = y_train.mean()

print("\n===== BASELINE MODEL =====")

print(
    "Average training delivery duration:",
    round(baseline_prediction, 2),
    "minutes"
)


# ============================================================
# 3. Predict the same average value for every test record
# ============================================================

y_pred = np.full(
    len(y_test),
    baseline_prediction
)


# ============================================================
# 4. Evaluate baseline model
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
# 5. Display results
# ============================================================

print("\n===== BASELINE RESULTS =====")

print("MAE:", round(mae, 2), "minutes")
print("RMSE:", round(rmse, 2), "minutes")


# ============================================================
# 6. Explanation
# ============================================================

print("\n===== INTERPRETATION =====")

print(
    "The baseline predicts the same average delivery time "
    "for every order."
)

print(
    "Our machine learning models should achieve lower "
    "MAE and RMSE than this baseline."
)