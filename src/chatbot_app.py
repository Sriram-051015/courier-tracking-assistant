from chatbot_engine import generate_response


# ============================================================
# Interactive AI Courier Tracking Chatbot
# ============================================================

def start_chatbot():

    print("\n==============================================")
    print("      AI COURIER TRACKING ASSISTANT")
    print("==============================================")

    print("\nHello! 👋")
    print("I can help you with:")
    print("- Shipment status")
    print("- Delivery time")
    print("- Tracking information")
    print("- Customer support")

    print("\nType 'exit' to close the chatbot.")

    while True:

        print("\n" + "-" * 60)

        user_query = input("Customer: ")

        if user_query.lower().strip() == "exit":

            print("\nAssistant: Thank you for using the AI Courier")
            print("Assistant: Tracking Assistant. Have a great day! 👋")

            break

        if not user_query.strip():

            print(
                "Assistant: Please enter a question "
                "or provide a tracking ID."
            )

            continue

        response = generate_response(user_query)

        print("\nAssistant:")
        print(response)


# ============================================================
# Start chatbot
# ============================================================

if __name__ == "__main__":

    start_chatbot()