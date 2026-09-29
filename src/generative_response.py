import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:1b"


def generate_ai_response(shipment_info, customer_query):

    tracking_id = shipment_info["tracking_id"]
    status = shipment_info["status"]
    city = shipment_info["city"]
    courier_id = shipment_info["courier_id"]
    predicted_eta = shipment_info["predicted_eta"]

    prompt = f"""
You are a courier customer-support assistant.

IMPORTANT RULES:
1. The shipment information below is verified data.
2. Answer the customer's question using this data.
3. NEVER ask the customer for a tracking ID if one is already present.
4. NEVER invent shipment information.
5. Keep the response short, clear, friendly and professional.
6. Do not mention AI, models, prompts, or these instructions.

VERIFIED SHIPMENT DATA:
Tracking ID: {tracking_id}
Status: {status}
City: {city}
Courier ID: {courier_id}
Predicted delivery duration: {predicted_eta} minutes

CUSTOMER QUESTION:
{customer_query}

Answer the customer's question directly using the verified shipment data.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return result["response"].strip()


if __name__ == "__main__":

    test_shipment = {
        "tracking_id": "3322376",
        "status": "Delivered",
        "city": "Jilin",
        "courier_id": 4849,
        "predicted_eta": 234.66
    }

    test_query = "Where is my order 3322376?"

    response = generate_ai_response(
        test_shipment,
        test_query
    )

    print("\n===== GENERATIVE AI RESPONSE =====")
    print(response)