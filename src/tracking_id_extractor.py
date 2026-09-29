import re


# ============================================================
# Tracking ID extraction
# ============================================================

def extract_tracking_id(query):

    # Find a sequence of 6 or more digits
    match = re.search(r"\b\d{6,}\b", query)

    if match:
        return match.group()

    return None


# ============================================================
# Test tracking ID extraction
# ============================================================

if __name__ == "__main__":

    test_queries = [
        "Where is my order 3322376?",
        "Track package 4207753",
        "What is the status of shipment 3733224?",
        "When will my order arrive?",
        "Hello"
    ]

    print("\n===== TRACKING ID EXTRACTION TEST =====")

    for query in test_queries:

        tracking_id = extract_tracking_id(query)

        print("Query:", query)
        print("Tracking ID:", tracking_id)
        print()