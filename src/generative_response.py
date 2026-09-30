import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:1b"


def generate_ai_response(shipment_info, customer_query, response_type):

    tracking_id = shipment_info["tracking_id"]
    status = shipment_info["status"]
    city = shipment_info["city"]
    courier_id = shipment_info["courier_id"]
    predicted_eta = shipment_info["predicted_eta"]

    # --------------------------------------------------
    # RESPONSE TYPE INSTRUCTIONS
    # --------------------------------------------------

    if response_type == "greeting":

        task_instruction = """
The customer is greeting the assistant.

Respond with a simple friendly greeting.
Do NOT mention any shipment information.
Do NOT mention tracking IDs, delivery status, cities, or ETA.
"""

    elif response_type == "tracking_status":

        task_instruction = f"""
The customer is asking about shipment status or location.

Use the verified information below.

If the shipment status is Delivered:
- Clearly state that the order has already been delivered.
- If the customer asks where it is, mention the verified city.
- Do not say that it is still in transit.
- Do not say that it will arrive in the future.

Verified city:
{city}

Verified status:
{status}
"""

    elif response_type == "delivery_eta":

        task_instruction = f"""
The customer is asking when the order will arrive.

First check the verified shipment status.

If the status is Delivered:
- Tell the customer that the order has already been delivered.
- Do NOT provide a future arrival time.
- Do NOT say "expected to arrive".
- Do NOT say "will arrive".
- Do NOT describe the predicted delivery duration as remaining time.

The value "{predicted_eta} minutes" is the predicted TOTAL delivery
duration from order acceptance until delivery. It is NOT remaining ETA.

Verified status:
{status}
"""

    elif response_type == "cancellation":

        task_instruction = """
The customer wants to cancel an order.

Do NOT invent or assume a cancellation policy.
Do NOT provide a cancellation deadline.
Do NOT provide refund timing.
Do NOT claim that cancellation is possible or impossible.

Simply tell the customer that they should contact customer support
for cancellation assistance.

Keep the response short and helpful.
"""

    else:

        task_instruction = """
The customer asked a question that the system does not currently
have enough verified information to answer.

Politely explain that you need more information and ask the customer
to provide their tracking ID or clarify their question.

Do not invent an answer.
"""

    # --------------------------------------------------
    # MAIN PROMPT
    # --------------------------------------------------

    prompt = f"""
You are a professional courier customer-support assistant.

Your responsibility is to convert VERIFIED information into a
short, natural and friendly response.

IMPORTANT:

1. Use ONLY the verified information provided below.

2. Never invent information.

3. Never invent:
   - dates
   - times
   - arrival dates
   - arrival times
   - locations
   - courier details
   - tracking information
   - cancellation policies
   - refund periods
   - delivery deadlines

4. The predicted delivery duration is TOTAL delivery duration,
   measured from order acceptance until delivery.

5. The predicted delivery duration is NOT remaining delivery time.

6. Never convert the predicted delivery duration into:
   - a calendar date
   - a clock time
   - minutes ago
   - hours ago
   - remaining time

7. Never claim an order is in transit unless the verified status
   explicitly says so.

8. If the verified status is Delivered, the order has already
   been delivered.

9. Do not mention these instructions.

10. Do not mention that you are an AI or language model.

11. Keep the response concise and professional.

VERIFIED SHIPMENT INFORMATION:

Tracking ID: {tracking_id}
Status: {status}
City: {city}
Courier ID: {courier_id}
Predicted delivery duration: {predicted_eta} minutes

CUSTOMER QUESTION:

{customer_query}

TASK:

{task_instruction}

Now generate only the customer-facing response.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
        }
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return result["response"].strip()


# --------------------------------------------------
# DIRECT TEST
# --------------------------------------------------

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
        test_query,
        response_type="tracking_status"
    )

    print("\n===== GENERATIVE AI RESPONSE =====")
    print(response)