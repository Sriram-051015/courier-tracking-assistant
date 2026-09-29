import pandas as pd

# ============================================================
# 1. Load cleaned dataset
# ============================================================

input_file = "data/processed/courier_tracking_cleaned.csv"
output_file = "data/processed/eta_features.csv"

df = pd.read_csv(input_file)

print("Original dataset shape:", df.shape)


# ============================================================
# 2. Select features available when an order is accepted
# ============================================================

features = [
    "region_id",
    "courier_id",
    "lng",
    "lat",
    "aoi_type",
    "accept_gps_valid",
    "accept_month",
    "accept_day",
    "accept_hour"
]

target = "delivery_duration_minutes"

model_df = df[features + [target]].copy()


# ============================================================
# 3. Convert GPS validity to numeric values
# ============================================================

model_df["accept_gps_valid"] = (
    model_df["accept_gps_valid"]
    .astype(int)
)


# ============================================================
# 4. Handle missing values
# ============================================================

numeric_columns = [
    "lng",
    "lat"
]

for column in numeric_columns:
    model_df[column] = model_df[column].fillna(
        model_df[column].median()
    )


# ============================================================
# 5. Remove rows with missing model values
# ============================================================

model_df = model_df.dropna()


# ============================================================
# 6. Separate features and target
# ============================================================

X = model_df[features]
y = model_df[target]


# ============================================================
# 7. Display feature information
# ============================================================

print("\n===== MODEL FEATURES =====")

print(X.columns.tolist())

print("\nNumber of features:", X.shape[1])

print("\nFeature data shape:", X.shape)

print("Target data shape:", y.shape)


# ============================================================
# 8. Display missing values
# ============================================================

print("\n===== MISSING VALUES =====")

print(model_df.isnull().sum())


# ============================================================
# 9. Display sample data
# ============================================================

print("\n===== FEATURE SAMPLE =====")

print(model_df.head())


# ============================================================
# 10. Save feature dataset
# ============================================================

model_df.to_csv(output_file, index=False)

print("\nFeature dataset saved successfully:")
print(output_file)