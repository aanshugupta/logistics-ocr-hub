import streamlit as st
import pandas as pd
import os

st.title("📝 Verify & Edit Trip Details")

file_path = "data/trips.csv"

if not os.path.exists(file_path):
    st.warning("No data found!")
else:
    df = pd.read_csv(file_path)

    pending = df[df["status"] == "pending_verification"]

    if pending.empty:
        st.success("No pending records!")
    else:
        selected = st.selectbox("Select a pending record", pending["trip_id"].tolist())

        rec = pending[pending["trip_id"] == selected].iloc[0]

        trip_id = st.text_input("Trip ID", rec["trip_id"])
        invoice_no = st.text_input("Invoice No", rec["invoice_no"])
        driver = st.text_input("Driver", rec["driver"])
        vehicle = st.text_input("Vehicle No", rec["vehicle_no"])
        loading = st.text_input("Loading", rec["loading"])
        destination = st.text_input("Destination", rec["destination"])
        qty = st.text_input("Quantity", rec["quantity"])

        if st.button("Approve"):
            idx = df[df["trip_id"] == selected].index[0]

            df.loc[idx, "trip_id"] = trip_id
            df.loc[idx, "invoice_no"] = invoice_no
            df.loc[idx, "driver"] = driver
            df.loc[idx, "vehicle_no"] = vehicle
            df.loc[idx, "loading"] = loading
            df.loc[idx, "destination"] = destination
            df.loc[idx, "quantity"] = qty
            df.loc[idx, "status"] = "verified"

            df.to_csv(file_path, index=False)

            st.success("Record Verified!")
