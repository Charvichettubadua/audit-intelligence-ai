import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Direct Premium CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    
    /* CS Top Left Logo */
    .top-left-brand {
        font-size: 24px;
        font-weight: bold;
        color: #38bdf8;
        border: 2px solid #38bdf8;
        padding: 5px 20px;
        display: inline-block;
        margin-bottom: 20px;
    }

    .main-title {
        text-align: center;
        color: #38bdf8;
        letter-spacing: 5px;
        font-size: 40px;
        font-weight: 800;
    }
    
    .sub-title {
        text-align: center;
        color: #888;
        font-size: 18px;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. TOP ROW: CS LOGO (Left) & ROBOT (Center)
t1, t2, t3 = st.columns([1, 2, 1])
with t1:
    st.markdown('<div class="top-left-brand">C S</div>', unsafe_allow_html=True)

with t2:
    # Android Robot Center
    st.markdown("<center><img src='https://cdn-icons-png.flaticon.com/512/11516/11516905.png' width='100'></center>", unsafe_allow_html=True)
    st.markdown('<div class="main-title">RISKSHIELD COMMAND</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">CHARVI SRI | FORENSIC INTELLIGENCE</div>', unsafe_allow_html=True)

st.divider()

# 2. RISK IMAGES SECTION
st.markdown("### 🔍 Forensic Surveillance Metrics")
i1, i2, i3 = st.columns(3)
i1.image("https://images.unsplash.com/photo-1551288049-bbda48658a7d?w=400", caption="Neural Risk Mapping")
i2.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Transaction Anomaly")
i3.image("https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400", caption="AI Forensic Scan")

st.divider()

# 3. FILE UPLOADER
st.markdown("### 📥 Neural Data Ingestion")
uploaded_file = st.file_uploader("Upload Forensic Audit Ledger (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Data Authenticated. Real-time Stream Active.")
    st.dataframe(df.head(20), use_container_width=True)
else:
    st.info("System Ready. Please upload a forensic CSV file to begin analysis.")
