from customer_query import detect_intent
from tracking_id_extractor import extract_tracking_id
from tracking_assistant import track_shipment

from generative_response import generate_ai_response


def generate_response(query):

    intent = detect_intent(query)

    # GREETING
    if intent == "greeting":

        shipment_info = {
            "tracking_id": "N/A",
            "status": "N/A",
            "city": "N/A",
            "courier_id": "N/A",
            "predicted_eta": "N/A"
        }

        return generate_ai_response(
            shipment_info,
            query,
            response_type="greeting"
        )

    # TRACKING STATUS / DELIVERY ETA
    if intent in ["tracking_status", "delivery_eta"]:

        tracking_id = extract_tracking_id(query)

        if tracking_id is None:
            return (
                "Sure! Please provide your tracking ID "
                "so I can check your shipment information."
            )

        shipment = track_shipment(tracking_id)

        if shipment is None:
            return (
                "I couldn't find a shipment with that tracking ID. "
                "Please check the tracking ID and try again."
            )

        return generate_ai_response(
            shipment,
            query,
            response_type=intent
        )

    # ORDER CANCELLATION
    if intent == "order_cancellation":

        tracking_id = extract_tracking_id(query)

        shipment_info = {
            "tracking_id": tracking_id or "N/A",
            "status": "N/A",
            "city": "N/A",
            "courier_id": "N/A",
            "predicted_eta": "N/A"
        }

        return generate_ai_response(
            shipment_info,
            query,
            response_type="cancellation"
        )

    # UNKNOWN QUERY
    tracking_id = extract_tracking_id(query)

    shipment_info = {
        "tracking_id": tracking_id or "N/A",
        "status": "N/A",
        "city": "N/A",
        "courier_id": "N/A",
        "predicted_eta": "N/A"
    }

    return generate_ai_response(
        shipment_info,
        query,
        response_type="unknown"
    )


if __name__ == "__main__":

    test_queries = [
        "Hello",
        "Where is my order 3322376?",
        "What is the status of my shipment 3322376?",
        "When will my order 3322376 arrive?",
        "I want to cancel my order",
        "Where is my order?",
        "What is my tracking number?"
    ]

    print("\n===== AI COURIER CHATBOT WITH GENERATIVE AI =====")

    for query in test_queries:

        print("\nCustomer:")
        print(query)

        response = generate_response(query)

        print("\nAssistant:")
        print(response)

        print("\n" + "-" * 60)
