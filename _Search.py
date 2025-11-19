import streamlit as st
import pandas as pd
import os

st.title("🔍 Search Trips")

file_path = "data/trips.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)

    query = st.text_input("Search by Trip ID, Invoice, Driver, Vehicle")

    if query:
        results = df[df.apply(lambda x: x.astype(str).str.contains(query, case=False).any(), axis=1)]
        st.dataframe(results)

        if not results.empty:
            st.download_button("Download CSV", results.to_csv(index=False), "search_results.csv")
else:
    st.warning("No data found!")

