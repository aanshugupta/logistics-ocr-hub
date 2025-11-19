import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Logistics OCR Hub", layout="wide")

# ---------- GLOBAL UI STYLING ----------
st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

section[data-testid="stSidebar"] {
    background-color: #f8f9fa !important;
    padding-top: 30px;
}

h1, h2, h3, h4 {
    font-family: 'Segoe UI', sans-serif;
    font-weight: 700;
}

.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}

.alert-info {
    padding: 15px;
    border-radius: 10px;
    background-color: #e8f1ff;
    color: #1a3d7c;
}

</style>
""", unsafe_allow_html=True)


# -------------- SIDEBAR MENU --------------
with st.sidebar:
    st.markdown("<h2>📂 Navigation</h2>", unsafe_allow_html=True)
    st.page_link("app.py", label="🏠 Dashboard")
    st.page_link("pages/_Upload.py", label="📤 Upload Document")
    st.page_link("pages/_Verify.py", label="📝 Verify Data")
    st.page_link("pages/_Search.py", label="🔍 Search Trips")
    st.page_link("pages/_Reports.py", label="📊 Reports")


# -------------- DASHBOARD CONTENT --------------
st.title("📦 Logistics OCR Hub (MVP)")
st.write(
    "<h3 style='color:#555;'>Welcome, Aanshu! Start by uploading documents from the sidebar.</h3>",
    unsafe_allow_html=True
)

file_path = "data/trips.csv"

if not os.path.exists(file_path):
    st.markdown("<div class='alert-info'>No data found. Please upload a document first.</div>", unsafe_allow_html=True)

else:
    df = pd.read_csv(file_path)

    st.subheader("📊 Quick Stats")

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""<div class='card'><h3>{len(df)}</h3>Total Trips</div>""", unsafe_allow_html=True)
    col2.markdown(f"""<div class='card'><h3>{len(df[df['status']=='verified'])}</h3>Verified</div>""", unsafe_allow_html=True)
    col3.markdown(f"""<div class='card'><h3>{len(df[df['status']=='pending_verification'])}</h3>Pending</div>""", unsafe_allow_html=True)
