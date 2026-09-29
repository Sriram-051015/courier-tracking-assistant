import pandas as pd
import joblib


# ============================================================
# 1. Load saved model
# ============================================================

model = joblib.load(
    "models/eta_random_forest.pkl"
)

print("ETA model loaded successfully.")


# ============================================================
# 2. Load test data
# ============================================================

X_test = pd.read_csv(
    "data/processed/X_test.csv"
)

y_test = pd.read_csv(
    "data/processed/y_test.csv"
).squeeze()


# ============================================================
# 3. Convert categorical column
# ============================================================

X_test = pd.get_dummies(
    X_test,
    columns=["aoi_type"]
)


# ============================================================
# 4. Match model feature columns
# ============================================================

model_features = model.feature_names_in_

X_test = X_test.reindex(
    columns=model_features,
    fill_value=0
)


# ============================================================
# 5. Predict ETA
# ============================================================

predictions = model.predict(X_test)


# ============================================================
# 6. Display sample predictions
# ============================================================

print("\n===== SAMPLE ETA PREDICTIONS =====")

for i in range(10):

    print(
        f"Order {i + 1}: "
        f"Actual = {y_test.iloc[i]:.2f} minutes | "
        f"Predicted = {predictions[i]:.2f} minutes"
    )


# ============================================================
# 7. Display average predicted ETA
# ============================================================

print("\n===== ETA SUMMARY =====")

print(
    "Average predicted ETA:",
    round(predictions.mean(), 2),
    "minutes"
)

print(
    "Minimum predicted ETA:",
    round(predictions.min(), 2),
    "minutes"
)

print(
    "Maximum predicted ETA:",
    round(predictions.max(), 2),
    "minutes"
)