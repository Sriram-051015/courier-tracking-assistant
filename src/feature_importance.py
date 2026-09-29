import pandas as pd
import joblib
import matplotlib.pyplot as plt


# ============================================================
# 1. Load trained model
# ============================================================

model = joblib.load(
    "models/eta_random_forest.pkl"
)

print("Random Forest model loaded successfully.")


# ============================================================
# 2. Load training data
# ============================================================

X_train = pd.read_csv(
    "data/processed/X_train.csv"
)

X_train = pd.get_dummies(
    X_train,
    columns=["aoi_type"]
)


# ============================================================
# 3. Get feature importance
# ============================================================

importance = pd.DataFrame({
    "feature": X_train.columns,
    "importance": model.feature_importances_
})


# ============================================================
# 4. Sort features by importance
# ============================================================

importance = importance.sort_values(
    by="importance",
    ascending=False
)


# ============================================================
# 5. Display feature importance
# ============================================================

print("\n===== FEATURE IMPORTANCE =====")

print(importance.to_string(index=False))


# ============================================================
# 6. Save feature importance
# ============================================================

importance.to_csv(
    "results/feature_importance.csv",
    index=False
)


# ============================================================
# 7. Create chart
# ============================================================

plt.figure(figsize=(10, 6))

plt.barh(
    importance["feature"],
    importance["importance"]
)

plt.gca().invert_yaxis()

plt.title("Random Forest Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Feature")

plt.tight_layout()

plt.savefig(
    "results/feature_importance.png",
    dpi=300
)


print("\nFeature importance saved successfully:")
print("results/feature_importance.csv")
print("results/feature_importance.png")