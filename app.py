import streamlit as st
import pd
import numpy as np

# 1. Page Configuration (No Whitespace)
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# 2. Master CSS (Cleaning all messy elements)
st.markdown("""
    <style>
    /* Global Background and Colors */
    .stApp { background-color: #0d1117 !important; color: #c9d1d9 !important; }
    
    /* CS BRAND LOGO (Top Left) */
    .brand-logo { 
        position: fixed; top: 25px; left: 25px; font-size: 24px; font-weight: 800; 
        color: #38bdf8; border: 2px solid #38bdf8; padding: 5px 15px; 
        background: rgba(56, 189, 248, 0.1); border-radius: 5px; z-index: 999;
    }

    /* True Center Alignment - Forces EVERYTHING to Middle */
    .main .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
        text-align: center;
        margin: auto;
    }

    /* Smaller, Professional Auth Tabs and Inputs (Collegiate style) */
    input {
        background-color: #0d1117 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        border-radius: 8px !important;
        height: 35px !important; /* Smaller Height */
        text-align: center;
        width: 100% !important;
        max-width: 380px !important; /* Smaller Width */
        margin: auto;
    }

    /* Center Auth Section Labels Cyan color */
    [data-testid="stRadio"] div div div label {
        display: block;
        margin: auto;
        color: #58a6ff !important;
        font-weight: bold;
    }

    /* Primary Blue Buttons (Matching Video) */
    .stButton>button {
        background-color: #0066ff !important;
        color: white !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        height: 42px !important;
        border: none !important;
        margin-top: 10px;
    }
    .stButton>button:hover { background-color: #005cc5 !important; }
    
    /* Metrics Row Cards (Dashboard only) */
    .metric-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 10px;
    }

    /* Remove Streamlit default junk and spacing */
    header, footer { visibility: hidden; }
    div
