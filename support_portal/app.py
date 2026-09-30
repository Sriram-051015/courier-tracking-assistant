import sys
from pathlib import Path

import streamlit as st


# --------------------------------------------------
# PROJECT PATH
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from tracking_assistant import track_shipment
from chatbot_engine import generate_response


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Support Portal",
    page_icon="🎧",
    layout="centered"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎧 Customer Support Portal")

st.write(
    "Get assistance with your courier shipment and delivery."
)

st.divider()


# --------------------------------------------------
# TRACKING INFORMATION
# --------------------------------------------------

st.subheader("📦 Shipment Information")

tracking_id = st.text_input(
    "Tracking ID",
    placeholder="Example: 3322376"
)


if tracking_id:

    shipment = track_shipment(tracking_id.strip())

    if shipment is None:

        st.error(
            "Shipment not found. Please check your tracking ID."
        )

    else:

        st.success("Shipment found!")

        col1, col2 = st.columns(2)

        with col1:

            st.write("**Tracking ID**")

            st.write(shipment["tracking_id"])

            st.write("**Status**")

            st.write(shipment["status"])

            st.write("**City**")

            st.write(shipment["city"])

        with col2:

            st.write("**Courier ID**")

            st.write(shipment["courier_id"])

            st.write("**Region ID**")

            st.write(shipment["region_id"])

            st.write("**Delivery Duration**")

            st.write(
                f'{shipment["actual_delivery_duration"]:.2f} minutes'
            )


st.divider()


# --------------------------------------------------
# CUSTOMER SUPPORT REQUEST
# --------------------------------------------------

st.subheader("💬 Contact Customer Support")

customer_name = st.text_input(
    "Customer Name",
    placeholder="Enter your name"
)

issue_category = st.selectbox(
    "Issue Category",
    [
        "Shipment Status",
        "Delivery Delay",
        "Delivery Information",
        "Order Cancellation",
        "General Query"
    ]
)

customer_query = st.text_area(
    "Describe your issue",
    placeholder="Example: Where is my order?"
)


# --------------------------------------------------
# SUBMIT REQUEST
# --------------------------------------------------

if st.button("Submit Support Request", type="primary"):

    if not customer_name.strip():

        st.warning("Please enter your name.")

    elif not customer_query.strip():

        st.warning("Please describe your issue.")

    else:

        # Add tracking ID to the query when available
        if tracking_id.strip():

            complete_query = (
                f"{customer_query.strip()} "
                f"My tracking ID is {tracking_id.strip()}."
            )

        else:

            complete_query = customer_query.strip()

        with st.spinner("Preparing support response..."):

            try:

                response = generate_response(complete_query)

                st.success("Support request processed.")

                st.subheader("🤖 Support Response")

                st.write(response)

            except Exception:

                st.error(
                    "Sorry, we couldn't process your request right now. "
                    "Please try again."
                )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("🎧 Customer Support")

    st.write(
        """
        **Support Features**

        • Shipment lookup  
        • Delivery information  
        • Customer issue submission  
        • NLP-based query detection  
        • AI-generated support responses
        """
    )

    st.divider()

    st.write("**Technology Stack**")

    st.write(
        """
        Python  
        Streamlit  
        Pandas  
        NLP  
        Ollama  
        Gemma 3
        """
    )