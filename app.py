import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Logistics OCR Hub", layout="wide")

st.title("📦 Logistics OCR Hub (MVP)")

st.write("Welcome, Aanshu! Use the sidebar to upload documents, verify data, search trips, and download reports.")

# Show quick stats
if os.path.exists("data/trips.csv"):
    df = pd.read_csv("data/trips.csv")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Trips", len(df))
    col2.metric("Verified", len(df[df["status"] == "verified"]))
    col3.metric("Pending", len(df[df["status"] == "pending_verification"]))
else:
    st.info("No data found. Please upload a document first.")

