import re


# ============================================================
# Customer Query Intent Detection
# ============================================================

def detect_intent(query):

    query = query.lower().strip()

    # --------------------------------------------------------
    # Tracking / Status queries
    # --------------------------------------------------------

    tracking_keywords = [
        "where is my order",
        "where is my package",
        "where is my parcel",
        "track my order",
        "track my package",
        "track my parcel",
        "order status",
        "shipment status",
        "delivery status",
        "status of my order",
        "status of my shipment"
    ]

    # --------------------------------------------------------
    # ETA / Delivery time queries
    # --------------------------------------------------------

    eta_keywords = [
        "when will my order arrive",
        "when will my package arrive",
        "when will my parcel arrive",
        "when will it arrive",
        "when will my order be delivered",
        "when will my package be delivered",
        "how long will delivery take",
        "how long will it take",
        "delivery time",
        "estimated delivery",
        "eta"
    ]

    # ETA queries containing a tracking ID
    eta_patterns = [
        r"when will my order \d+ arrive",
        r"when will my package \d+ arrive",
        r"when will my parcel \d+ arrive",
        r"when will my order \d+ be delivered",
        r"when will my package \d+ be delivered"
    ]

    # --------------------------------------------------------
    # Cancellation queries
    # --------------------------------------------------------

    cancellation_keywords = [
        "cancel my order",
        "cancel order",
        "cancel my package",
        "cancel my parcel",
        "i want to cancel"
    ]

    # --------------------------------------------------------
    # Greeting queries
    # --------------------------------------------------------

    greeting_keywords = [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]

    # --------------------------------------------------------
    # Check tracking intent
    # --------------------------------------------------------

    for keyword in tracking_keywords:

        if keyword in query:
            return "tracking_status"

    # --------------------------------------------------------
    # Check ETA keyword intent
    # --------------------------------------------------------

    for keyword in eta_keywords:

        if keyword in query:
            return "delivery_eta"

    # --------------------------------------------------------
    # Check ETA pattern intent
    # --------------------------------------------------------

    for pattern in eta_patterns:

        if re.search(pattern, query):
            return "delivery_eta"

    # --------------------------------------------------------
    # Check cancellation intent
    # --------------------------------------------------------

    for keyword in cancellation_keywords:

        if keyword in query:
            return "order_cancellation"

    # --------------------------------------------------------
    # Check greeting intent
    # --------------------------------------------------------

    words = query.split()

    for keyword in greeting_keywords:

        if keyword in words:
            return "greeting"

    # --------------------------------------------------------
    # Unknown query
    # --------------------------------------------------------

    return "unknown"


# ============================================================
# Test customer queries
# ============================================================

if __name__ == "__main__":

    test_queries = [
        "Where is my order?",
        "What is the status of my shipment?",
        "When will my order arrive?",
        "How long will delivery take?",
        "Hello",
        "I want to cancel my order",
        "When will my order 3322376 arrive?"
    ]

    print("\n===== CUSTOMER QUERY INTENT TEST =====")

    for query in test_queries:

        intent = detect_intent(query)

        print(f"Query: {query}")
        print(f"Intent: {intent}")
        print()