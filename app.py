import streamlit as st
st.set_page_config(page_title="Logistics OCR Hub", layout="wide")

# Custom UI CSS
st.markdown("""
<style>

/* Main container padding */
.block-container {
    padding-top: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* Sidebar styling */
section[data-testid="stSidebar"] {
    background-color: #f8f9fa;
    padding-top: 30px;
}

/* Sidebar text */
section[data-testid="stSidebar"] .css-1d391kg {
    font-size: 18px;
}

/* Headings */
h1, h2, h3 {
    font-family: 'Segoe UI', sans-serif;
    font-weight: 700;
}

/* Cards */
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* Soft alert info */
.alert-info {
    padding: 15px;
    border-radius: 10px;
    background-color: #e8f1ff;
    color: #1a3d7c;
}

/* Tables */
table {
    border-radius: 8px;
}

</style>
""", unsafe_allow_html=True)
