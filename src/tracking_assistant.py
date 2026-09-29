import pandas as pd
import joblib


# ============================================================
# 1. Load tracking dataset
# ============================================================

DATA_FILE = "data/processed/courier_tracking_cleaned.csv"

df = pd.read_csv(DATA_FILE)


# ============================================================
# 2. Load ETA model
# ============================================================

MODEL_FILE = "models/eta_random_forest.pkl"

model = joblib.load(MODEL_FILE)


# ============================================================
# 3. Tracking lookup
# ============================================================

def find_order(order_id):

    result = df[
        df["order_id"].astype(str) == str(order_id)
    ]

    if result.empty:
        return None

    return result.iloc[0]


# ============================================================
# 4. Shipment status
# ============================================================

def get_status(order):

    if pd.notna(order["delivery_datetime"]):
        return "Delivered"

    elif pd.notna(order["accept_datetime"]):
        return "Order Accepted"

    else:
        return "Unknown"


# ============================================================
# 5. ETA prediction
# ============================================================

def predict_eta(order):

    features = pd.DataFrame([{
        "region_id": order["region_id"],
        "courier_id": order["courier_id"],
        "lng": order["lng"],
        "lat": order["lat"],
        "aoi_type": order["aoi_type"],
        "accept_gps_valid": int(order["accept_gps_valid"]),
        "accept_month": order["accept_month"],
        "accept_day": order["accept_day"],
        "accept_hour": order["accept_hour"]
    }])

    features = pd.get_dummies(
        features,
        columns=["aoi_type"]
    )

    features = features.reindex(
        columns=model.feature_names_in_,
        fill_value=0
    )

    prediction = model.predict(features)[0]

    return prediction


# ============================================================
# 6. Complete tracking response
# ============================================================

def track_shipment(order_id):

    order = find_order(order_id)

    if order is None:
        return None

    status = get_status(order)

    eta = predict_eta(order)

    return {
        "tracking_id": order["order_id"],
        "status": status,
        "city": order["city"],
        "courier_id": order["courier_id"],
        "region_id": order["region_id"],
        "acceptance_time": order["accept_time"],
        "delivery_time": order["delivery_time"],
        "actual_delivery_duration": order[
            "delivery_duration_minutes"
        ],
        "predicted_eta": eta
    }


# ============================================================
# 7. Test complete tracking assistant
# ============================================================

if __name__ == "__main__":

    test_order_id = df["order_id"].iloc[0]

    result = track_shipment(test_order_id)

    print("\n===== AI COURIER TRACKING ASSISTANT =====")

    if result is None:

        print("Tracking ID not found.")

    else:

        print("Tracking ID:",
              result["tracking_id"])

        print("Shipment Status:",
              result["status"])

        print("City:",
              result["city"])

        print("Courier ID:",
              result["courier_id"])

        print("Region ID:",
              result["region_id"])

        print("Acceptance Time:",
              result["acceptance_time"])

        print("Delivery Time:",
              result["delivery_time"])

        print(
            "Actual Delivery Duration:",
            round(result["actual_delivery_duration"], 2),
            "minutes"
        )

        print(
            "Predicted ETA:",
            round(result["predicted_eta"], 2),
            "minutes"
        )