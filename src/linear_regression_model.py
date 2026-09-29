import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
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
# 2. Convert categorical columns to numeric
# ============================================================

categorical_columns = [
    "aoi_type"
]

X_train = pd.get_dummies(
    X_train,
    columns=categorical_columns
)

X_test = pd.get_dummies(
    X_test,
    columns=categorical_columns
)


# Make sure both datasets have the same columns
X_test = X_test.reindex(
    columns=X_train.columns,
    fill_value=0
)


# ============================================================
# 3. Train Linear Regression model
# ============================================================

model = LinearRegression()

model.fit(
    X_train,
    y_train
)


# ============================================================
# 4. Make predictions
# ============================================================

y_pred = model.predict(X_test)


# ============================================================
# 5. Evaluate model
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
# 6. Display results
# ============================================================

print("\n===== LINEAR REGRESSION RESULTS =====")

print("MAE:", round(mae, 2), "minutes")

print("RMSE:", round(rmse, 2), "minutes")


# ============================================================
# 7. Compare with baseline
# ============================================================

baseline_mae = 108.46
baseline_rmse = 147.31

print("\n===== BASELINE COMPARISON =====")

print("Baseline MAE:", baseline_mae, "minutes")
print("Linear Regression MAE:", round(mae, 2), "minutes")

print("\nBaseline RMSE:", baseline_rmse, "minutes")
print("Linear Regression RMSE:", round(rmse, 2), "minutes")


if mae < baseline_mae:
    print("\nLinear Regression improved the baseline.")
else:
    print("\nLinear Regression did not improve the baseline.")