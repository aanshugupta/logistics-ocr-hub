import streamlit as st
import pandas as pd
from google import genai
import os
import datetime

st.title("📤 Upload Trip Document")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

uploaded = st.file_uploader("Upload PDF or Image", type=["jpg", "png", "jpeg", "pdf"])

if uploaded:
    st.image(uploaded, width=300)

    st.info("Extracting data... Please wait...")

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            "Extract Trip details (Trip ID, Invoice No, Driver, Vehicle No, Loading, "
            "Destination, Quantity) in clean JSON format.",
            genai.types.Part.from_file(uploaded)
        ]
    )

    st.subheader("Extracted Data")
    st.json(response.text)

    extracted = eval(response.text)

    df = pd.DataFrame([{
        "trip_id": extracted.get("trip_id"),
        "invoice_no": extracted.get("invoice_no"),
        "driver": extracted.get("driver"),
        "vehicle_no": extracted.get("vehicle_no"),
        "loading": extracted.get("loading"),
        "destination": extracted.get("destination"),
        "quantity": extracted.get("quantity"),
        "status": "pending_verification",
        "file_url": uploaded.name,
        "timestamp": datetime.datetime.now()
    }])

    os.makedirs("data", exist_ok=True)
    file_path = "data/trips.csv"

    if not os.path.exists(file_path):
        df.to_csv(file_path, index=False)
    else:
        old = pd.read_csv(file_path)
        new = pd.concat([old, df], ignore_index=True)
        new.to_csv(file_path, index=False)

    st.success("Document added to verification queue!")
