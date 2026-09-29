import pandas as pd


# ============================================================
# 1. Load courier tracking dataset
# ============================================================

DATA_FILE = "data/processed/courier_tracking_cleaned.csv"

df = pd.read_csv(DATA_FILE)


# ============================================================
# 2. Tracking lookup function
# ============================================================

def track_order(order_id):

    result = df[
        df["order_id"].astype(str) == str(order_id)
    ]

    if result.empty:
        return None

    return result.iloc[0]


# ============================================================
# 3. Test tracking lookup
# ============================================================

if __name__ == "__main__":

    test_order_id = df["order_id"].iloc[0]

    order = track_order(test_order_id)

    print("\n===== TRACKING TEST =====")

    if order is None:

        print("Order not found.")

    else:

        print("Tracking ID:", order["order_id"])
        print("Courier ID:", order["courier_id"])
        print("Region ID:", order["region_id"])
        print("City:", order["city"])
        print("Acceptance Time:", order["accept_time"])
        print("Delivery Time:", order["delivery_time"])
        print(
            "Delivery Duration:",
            order["delivery_duration_minutes"],
            "minutes"
        )