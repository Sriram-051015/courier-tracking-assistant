import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 1. Load cleaned dataset
# ============================================================

input_file = "data/processed/courier_tracking_cleaned.csv"

df = pd.read_csv(input_file)

print("Dataset shape:", df.shape)


# ============================================================
# 2. Basic delivery statistics
# ============================================================

print("\n===== DELIVERY DURATION STATISTICS =====")

print(
    df["delivery_duration_minutes"].describe()
)


# ============================================================
# 3. Courier statistics
# ============================================================

print("\n===== COURIER STATISTICS =====")

print("Number of unique couriers:",
      df["courier_id"].nunique())

print("\nTop 10 couriers by number of deliveries:")

print(
    df["courier_id"]
    .value_counts()
    .head(10)
)


# ============================================================
# 4. Region statistics
# ============================================================

print("\n===== REGION STATISTICS =====")

print("Number of regions:",
      df["region_id"].nunique())

print("\nTop 10 regions by deliveries:")

print(
    df["region_id"]
    .value_counts()
    .head(10)
)


# ============================================================
# 5. Delivery duration by hour
# ============================================================

hourly_delivery = (
    df.groupby("accept_hour")["delivery_duration_minutes"]
    .mean()
    .sort_index()
)

print("\n===== AVERAGE DELIVERY TIME BY ACCEPTANCE HOUR =====")

print(hourly_delivery)


# ============================================================
# 6. Delivery duration by month
# ============================================================

monthly_delivery = (
    df.groupby("accept_month")["delivery_duration_minutes"]
    .mean()
    .sort_index()
)

print("\n===== AVERAGE DELIVERY TIME BY MONTH =====")

print(monthly_delivery)


# ============================================================
# 7. Plot delivery duration distribution
# ============================================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df["delivery_duration_minutes"],
    bins=50,
    kde=True
)

plt.title("Delivery Duration Distribution")
plt.xlabel("Delivery Duration (Minutes)")
plt.ylabel("Number of Orders")

plt.tight_layout()

plt.savefig(
    "results/delivery_duration_distribution.png",
    dpi=300
)



# ============================================================
# 8. Plot average delivery time by hour
# ============================================================

plt.figure(figsize=(10, 6))

hourly_delivery.plot(
    kind="line",
    marker="o"
)

plt.title("Average Delivery Time by Acceptance Hour")
plt.xlabel("Acceptance Hour")
plt.ylabel("Average Delivery Duration (Minutes)")
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "results/average_delivery_by_hour.png",
    dpi=300
)


# ============================================================
# 9. Plot average delivery time by month
# ============================================================

plt.figure(figsize=(10, 6))

monthly_delivery.plot(
    kind="bar"
)

plt.title("Average Delivery Time by Month")
plt.xlabel("Month")
plt.ylabel("Average Delivery Duration (Minutes)")

plt.tight_layout()

plt.savefig(
    "results/average_delivery_by_month.png",
    dpi=300
)



# ============================================================
# 10. Save summary tables
# ============================================================

hourly_delivery.to_csv(
    "results/average_delivery_by_hour.csv"
)

monthly_delivery.to_csv(
    "results/average_delivery_by_month.csv"
)

print("\n===== EDA COMPLETED =====")

print("Charts saved in:")
print("results/")

print("\nSummary files saved:")
print("results/average_delivery_by_hour.csv")
print("results/average_delivery_by_month.csv")