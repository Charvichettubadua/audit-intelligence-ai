import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Premium Global CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    
    /* CS Top Left Logo */
    .top-left-logo {
        position: fixed;
        top: 40px;
        left: 20px;
        font-size: 22px;
        font-weight: bold;
        color: #38bdf8;
        border: 2px solid #38bdf8;
        padding: 5px 15px;
        letter-spacing: 5px;
        z-index: 999;
    }

    /* Center Robot Container */
    .robot-header {
        text-align: center;
        margin-top: -30px;
        margin-bottom: 20px;
    }

    /* Main Title */
    .main-title {
        text-align: center;
        color: #38bdf8;
        letter-spacing: 8px;
        font-size: 45px;
        font-weight: 800;
        margin-bottom: 5px;
    }
    
    .sub-text {
        text-align: center;
        color: #888;
        font-size: 18px;
        margin-bottom: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- TOP SECTION: CS LOGO & ROBOT ---
st.markdown('<div class="top-left-logo">C S</div>', unsafe_allow_html=True)

# Android Robot Center
st.markdown('<div class="robot-header"><img src="https://cdn-icons-png.flaticon.com/512/11516/11516905.png" width="100"></div>', unsafe_allow_html=True)

# Titles
st.markdown('<div class="main-title">RISKSHIELD COMMAND CENTER</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">CHARVI SRI | ENTERPRISE FORENSIC INTELLIGENCE</div>', unsafe_allow_html=True)

st.divider()

# --- MIDDLE SECTION: RISK SURVEILLANCE IMAGES ---
st.markdown("### 🔍 Forensic Surveillance Metrics")
i1, i2, i3 = st.columns(3)
with i1:
    st.image("https://images.unsplash.com/photo-1551288049-bbda48658a7d?w=400", caption="Neural Risk Mapping")
with i2:
    st.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="High-Risk Transaction Flow")
with i3:
    st.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", caption="AI Forensic Scan")

st.divider()

# --- BOTTOM SECTION: DATA INGESTION ---
st.markdown("### 📥 Neural Data Ingestion")
uploaded_file = st.file_uploader("Upload Forensic Audit Ledger (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("
