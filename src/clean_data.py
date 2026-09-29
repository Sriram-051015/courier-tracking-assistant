import pandas as pd

# ============================================================
# 1. Load raw dataset
# ============================================================

input_file = "data/raw/delivery_jl.parquet"
output_file = "data/processed/courier_tracking_cleaned.csv"

df = pd.read_parquet(input_file)

print("Original dataset shape:", df.shape)


# ============================================================
# 2. Convert time columns
# ============================================================

df["accept_datetime"] = pd.to_datetime(
    df["accept_time"],
    format="%m-%d %H:%M:%S"
)

df["delivery_datetime"] = pd.to_datetime(
    df["delivery_time"],
    format="%m-%d %H:%M:%S"
)


# ============================================================
# 3. Calculate delivery duration
# ============================================================

df["delivery_duration_minutes"] = (
    df["delivery_datetime"] - df["accept_datetime"]
).dt.total_seconds() / 60


df["delivery_duration_hours"] = (
    df["delivery_duration_minutes"] / 60
)


# ============================================================
# 4. Check for invalid delivery durations
# ============================================================

print("\n===== DELIVERY DURATION CHECK =====")

print("Minimum duration:",
      df["delivery_duration_minutes"].min())

print("Maximum duration:",
      df["delivery_duration_minutes"].max())

print("Negative durations:",
      (df["delivery_duration_minutes"] < 0).sum())


# ============================================================
# 5. Check GPS coordinates
# ============================================================

df["accept_gps_valid"] = (
    df["accept_gps_lng"].notna()
    & df["accept_gps_lat"].notna()
    & (df["accept_gps_lng"] != 0)
    & (df["accept_gps_lat"] != 0)
)

df["delivery_gps_valid"] = (
    (df["delivery_gps_lng"] != 0)
    & (df["delivery_gps_lat"] != 0)
)


print("\n===== GPS CHECK =====")

print("Missing/invalid acceptance GPS:",
      (~df["accept_gps_valid"]).sum())

print("Missing/invalid delivery GPS:",
      (~df["delivery_gps_valid"]).sum())


# ============================================================
# 6. Extract useful date information
# ============================================================

df["accept_month"] = df["accept_datetime"].dt.month
df["accept_day"] = df["accept_datetime"].dt.day
df["accept_hour"] = df["accept_datetime"].dt.hour

df["delivery_month"] = df["delivery_datetime"].dt.month
df["delivery_day"] = df["delivery_datetime"].dt.day
df["delivery_hour"] = df["delivery_datetime"].dt.hour


# ============================================================
# 7. Remove invalid delivery durations
# ============================================================

before_rows = len(df)

df = df[df["delivery_duration_minutes"] >= 0].copy()

after_rows = len(df)

print("\nRows removed due to invalid duration:",
      before_rows - after_rows)


# ============================================================
# 8. Display cleaned dataset information
# ============================================================

print("\n===== CLEANED DATASET =====")
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())


# ============================================================
# 9. Save cleaned dataset
# ============================================================

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully:")
print(output_file)