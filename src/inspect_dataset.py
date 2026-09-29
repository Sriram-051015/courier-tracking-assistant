import pandas as pd

# Dataset path
file_path = "data/raw/delivery_jl.parquet"

# Load dataset
df = pd.read_parquet(file_path)

# Basic information
print("\n===== DATASET SHAPE =====")
print(df.shape)

# Column names
print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

# First 5 rows
print("\n===== FIRST 5 ROWS =====")
print(df.head())

# Dataset information
print("\n===== DATASET INFO =====")
df.info()

# Missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Duplicate rows
print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# Basic statistics
print("\n===== BASIC STATISTICS =====")
print(df.describe(include="all"))