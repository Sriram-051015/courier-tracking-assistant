# ============================================================
# AI Response Generator
# ============================================================


def generate_tracking_response(shipment):

    if shipment is None:

        return (
            "I couldn't find a shipment with the provided "
            "tracking ID. Please check the tracking ID and "
            "try again."
        )

    tracking_id = shipment["tracking_id"]
    status = shipment["status"]
    city = shipment["city"]
    courier_id = shipment["courier_id"]

    if status == "Delivered":

        return (
            f"Your shipment with tracking ID {tracking_id} "
            f"has been delivered successfully in {city}. "
            f"The shipment was handled by courier {courier_id}."
        )

    elif status == "Order Accepted":

        return (
            f"Your shipment with tracking ID {tracking_id} "
            f"has been accepted and is currently being "
            f"processed in {city}."
        )

    else:

        return (
            f"Your shipment with tracking ID {tracking_id} "
            f"is currently being processed."
        )


# ============================================================
# ETA Response
# ============================================================

def generate_eta_response(shipment):

    if shipment is None:

        return (
            "I couldn't find a shipment with the provided "
            "tracking ID."
        )

    tracking_id = shipment["tracking_id"]
    status = shipment["status"]
    eta = shipment["predicted_eta"]

    # Historical records are already completed deliveries.
    if status == "Delivered":

        return (
            f"Tracking ID {tracking_id} has already been "
            f"delivered. The machine learning model estimated "
            f"the delivery duration at approximately "
            f"{round(eta, 2)} minutes."
        )

    return (
        f"For tracking ID {tracking_id}, the estimated "
        f"delivery duration is approximately "
        f"{round(eta, 2)} minutes."
    )


# ============================================================
# Greeting Response
# ============================================================

def generate_greeting_response():

    return (
        "Hello! 👋 I'm your AI Courier Tracking Assistant. "
        "I can help you check shipment status and estimated "
        "delivery time. Please provide your tracking ID."
    )


# ============================================================
# Cancellation Response
# ============================================================

def generate_cancellation_response():

    return (
        "I can help with your cancellation request. "
        "Please contact customer support to confirm whether "
        "your shipment can still be cancelled."
    )


# ============================================================
# Test response generator
# ============================================================

if __name__ == "__main__":

    test_shipment = {
        "tracking_id": "3322376",
        "status": "Delivered",
        "city": "Jilin",
        "courier_id": 4849,
        "predicted_eta": 234.66
    }

    print("\n===== RESPONSE GENERATOR TEST =====")

    print("\nTracking Response:")
    print(generate_tracking_response(test_shipment))

    print("\nETA Response:")
    print(generate_eta_response(test_shipment))

    print("\nGreeting Response:")
    print(generate_greeting_response())

    print("\nCancellation Response:")
    print(generate_cancellation_response())