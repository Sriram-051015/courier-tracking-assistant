from customer_query import detect_intent
from tracking_id_extractor import extract_tracking_id
from tracking_assistant import track_shipment

from generative_response import generate_ai_response


def generate_response(query):

    intent = detect_intent(query)

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
            query
        )

    tracking_id = extract_tracking_id(query)

    if intent in ["tracking_status", "delivery_eta"]:

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
            query
        )

    if intent == "order_cancellation":

        shipment_info = {
            "tracking_id": tracking_id or "N/A",
            "status": "N/A",
            "city": "N/A",
            "courier_id": "N/A",
            "predicted_eta": "N/A"
        }

        return generate_ai_response(
            shipment_info,
            query
        )

    return generate_ai_response(
        {
            "tracking_id": tracking_id or "N/A",
            "status": "N/A",
            "city": "N/A",
            "courier_id": "N/A",
            "predicted_eta": "N/A"
        },
        query
    )


if __name__ == "__main__":

    test_queries = [
        "Hello",
        "Where is my order 3322376?",
        "What is the status of my shipment 3322376?",
        "When will my order 3322376 arrive?",
        "I want to cancel my order"
    ]

    print("\n===== AI COURIER CHATBOT WITH GENERATIVE AI =====")

    for query in test_queries:

        print("\nCustomer:")
        print(query)

        response = generate_response(query)

        print("\nAssistant:")
        print(response)

        print("\n" + "-" * 60)