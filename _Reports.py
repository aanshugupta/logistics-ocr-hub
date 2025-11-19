import streamlit as st
import pandas as pd
import os

st.title("📊 Reports")

file_path = "data/trips.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    st.write("### Verified Trips")
    verified = df[df["status"] == "verified"]
    st.dataframe(verified)

    st.download_button("Download Verified CSV", verified.to_csv(index=False), "verified_trips.csv")

    st.write("### Simple Summary")
    st.metric("Total Trips", len(df))
    st.metric("Verified", len(verified))
    st.metric("Pending", len(df[df["status"] == 'pending_verification']))
else:
    st.warning("No data found!")

