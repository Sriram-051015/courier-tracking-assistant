import sys
from pathlib import Path

import streamlit as st


# Add src folder to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from chatbot_engine import generate_response


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Courier Tracking Assistant",
    page_icon="📦",
    layout="centered"
)


# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666666;
        margin-bottom: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">📦 AI Courier Tracking Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Track shipments and get AI-powered customer support</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# INFORMATION PANEL
# --------------------------------------------------

with st.expander("ℹ️ What can I ask?"):

    st.write(
        """
        You can ask the assistant about:

        • Shipment status  
        • Tracking information  
        • Delivery time  
        • Order cancellation  
        • General courier support
        """
    )


# --------------------------------------------------
# DISPLAY PREVIOUS MESSAGES
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

user_query = st.chat_input(
    "Ask about your shipment..."
)


if user_query:

    # Display customer message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_query
        }
    )

    with st.chat_message("user"):
        st.write(user_query)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Checking shipment information..."):

            try:

                response = generate_response(user_query)

                st.write(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as error:

                error_message = (
                    "Sorry, I couldn't process your request right now. "
                    "Please try again."
                )

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("🚚 Courier Assistant")

    st.write(
        """
        **AI Features**

        • NLP intent detection  
        • Tracking ID extraction  
        • Shipment lookup  
        • ML-based delivery duration prediction  
        • Generative AI responses  
        • Customer support
        """
    )

    st.divider()

    st.write("**Technology Stack**")

    st.write(
        """
        Python  
        Streamlit  
        Scikit-learn  
        Ollama  
        Gemma 3  
        Pandas
        """
    )

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()