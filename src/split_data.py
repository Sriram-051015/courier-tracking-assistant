import pandas as pd
from sklearn.model_selection import train_test_split

# ============================================================
# 1. Load feature dataset
# ============================================================

input_file = "data/processed/eta_features.csv"

df = pd.read_csv(input_file)

print("Dataset shape:", df.shape)


# ============================================================
# 2. Separate features and target
# ============================================================

X = df.drop("delivery_duration_minutes", axis=1)

y = df["delivery_duration_minutes"]


# ============================================================
# 3. Split dataset into training and testing data
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# ============================================================
# 4. Display split information
# ============================================================

print("\n===== DATA SPLIT =====")

print("Total records:", len(df))

print("Training records:", len(X_train))

print("Testing records:", len(X_test))

print("Training percentage:",
      round(len(X_train) / len(df) * 100, 2), "%")

print("Testing percentage:",
      round(len(X_test) / len(df) * 100, 2), "%")


# ============================================================
# 5. Display feature columns
# ============================================================

print("\n===== FEATURES =====")

print(X_train.columns.tolist())


# ============================================================
# 6. Save split datasets
# ============================================================

X_train.to_csv(
    "data/processed/X_train.csv",
    index=False
)

X_test.to_csv(
    "data/processed/X_test.csv",
    index=False
)

y_train.to_csv(
    "data/processed/y_train.csv",
    index=False
)

y_test.to_csv(
    "data/processed/y_test.csv",
    index=False
)


print("\n===== FILES SAVED =====")

print("X_train.csv")
print("X_test.csv")
print("y_train.csv")
print("y_test.csv")