import sys
from pathlib import Path

import pandas as pd
import streamlit as st


# --------------------------------------------------
# PROJECT PATH
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "courier_tracking_cleaned.csv"
)

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "eta_random_forest.pkl"
)

SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))

from tracking_assistant import track_shipment


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Courier Tracking Dashboard",
    page_icon="📦",
    layout="wide"
)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv(DATA_PATH)

    return df


df = load_data()


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📦 Courier Tracking Dashboard")

st.write(
    "Track shipments and view verified delivery information."
)


# --------------------------------------------------
# KEY INFORMATION
# --------------------------------------------------

total_shipments = len(df)

total_couriers = df["courier_id"].nunique()

total_regions = df["region_id"].nunique()

average_duration = df["delivery_duration_minutes"].mean()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Shipments",
        f"{total_shipments:,}"
    )

with col2:
    st.metric(
        "Total Couriers",
        f"{total_couriers:,}"
    )

with col3:
    st.metric(
        "Total Regions",
        f"{total_regions:,}"
    )

with col4:
    st.metric(
        "Avg Delivery Duration",
        f"{average_duration:.1f} min"
    )


st.divider()


# --------------------------------------------------
# TRACKING SEARCH
# --------------------------------------------------

st.subheader("🔍 Track a Shipment")

tracking_id = st.text_input(
    "Enter Tracking ID",
    placeholder="Example: 3322376"
)


if tracking_id:

    shipment = track_shipment(tracking_id.strip())

    if shipment is None:

        st.error(
            "Shipment not found. Please check the tracking ID."
        )

    else:

        st.success("Shipment found!")

        st.subheader("Shipment Information")

        col1, col2, col3 = st.columns(3)

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

            st.write("**Acceptance Time**")

            st.write(shipment["acceptance_time"])

        with col3:

            st.write("**Delivery Time**")

            st.write(shipment["delivery_time"])

            st.write("**Actual Delivery Duration**")

            st.write(
                f'{shipment["actual_delivery_duration"]:.2f} minutes'
            )

            st.write("**Predicted Delivery Duration**")

            st.write(
                f'{shipment["predicted_eta"]:.2f} minutes'
            )


st.divider()


# --------------------------------------------------
# DATASET INFORMATION
# --------------------------------------------------

st.subheader("📊 Dataset Information")

st.write(
    f"The dashboard is currently connected to "
    f"**{total_shipments:,} historical shipment records**."
)

st.write(
    f"Data contains shipments from "
    f"**{total_regions} regions** and "
    f"**{total_couriers} couriers**."
)


# --------------------------------------------------
# RECENT SHIPMENTS
# --------------------------------------------------

st.subheader("📋 Shipment Records")

display_columns = [
    "order_id",
    "region_id",
    "city",
    "courier_id",
    "accept_time",
    "delivery_time",
    "delivery_duration_minutes"
]

available_columns = [
    column
    for column in display_columns
    if column in df.columns
]

st.dataframe(
    df[available_columns].head(20),
    use_container_width=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("🚚 Courier Dashboard")

    st.write(
        """
        **Dashboard Features**

        • Shipment tracking  
        • Courier information  
        • Region information  
        • Delivery duration  
        • Predicted delivery duration  
        • Historical shipment records
        """
    )

    st.divider()

    st.write("**Technology Stack**")

    st.write(
        """
        Python  
        Streamlit  
        Pandas  
        Scikit-learn  
        Random Forest
        """
    )