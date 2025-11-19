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

    st.write("### Summary")
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Trips", len(df))
    col2.metric("Verified", len(verified))
    col3.metric("Pending", len(df[df["status"]=='pending_verification']))

else:
    st.warning("No data found!")
