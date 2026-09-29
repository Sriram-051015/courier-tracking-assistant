import pandas as pd


# ============================================================
# 1. Load tracking dataset
# ============================================================

DATA_FILE = "data/processed/courier_tracking_cleaned.csv"

df = pd.read_csv(DATA_FILE)


# ============================================================
# 2. Shipment status function
# ============================================================

def get_shipment_status(order):

    if pd.notna(order["delivery_datetime"]):
        return "Delivered"

    elif pd.notna(order["accept_datetime"]):
        return "Order Accepted"

    else:
        return "Unknown"


# ============================================================
# 3. Test shipment status
# ============================================================

if __name__ == "__main__":

    test_order_id = df["order_id"].iloc[0]

    result = df[
        df["order_id"].astype(str) == str(test_order_id)
    ]

    if result.empty:

        print("Order not found.")

    else:

        order = result.iloc[0]

        status = get_shipment_status(order)

        print("\n===== SHIPMENT STATUS TEST =====")

        print("Tracking ID:", order["order_id"])
        print("Shipment Status:", status)