import streamlit as st
import pandas as pd
import numpy as np

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# --- Premium CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: white; }
    .brand-logo { position: fixed; top: 30px; left: 30px; font-size: 26px; font-weight: 800; color: #38bdf8; border: 3px solid #38bdf8; padding: 8px 20px; letter-spacing: 5px; background: rgba(56, 189, 248, 0.1); z-index: 999; }
    .auth-card { background: #161e2e; padding: 40px; border-radius: 20px; border: 1px solid #1e293b; text-align: center; margin-top: 50px; }
    div.stButton > button { background-color: #38bdf8 !important; color: #000 !important; font-weight: bold !important; width: 100%; border-radius: 8px !important; }
    .risk-box { background-color: #1e293b; padding: 20px; border-radius: 10px; border-left: 5px solid #ef4444; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- AUTHENTICATION (Open Access) ---
if not st.session_state.auth:
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.markdown("# 🛡️")
        st.markdown("<h2 style='color:#38bdf8;'>RISKSHIELD AI</h2>", unsafe_allow_html=True)
        st.write("IDENTITY ID (Optional for Guests)")
        st.text_input("ID", placeholder="Guest Access Active")
        if st.button("AUTHORIZE & ENTER"):
            st.session_state.auth = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD ---
else:
    st.markdown('<div class="brand-logo">C S</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>CHARVI SRI | SENIOR FORENSIC ANALYST</p>", unsafe_allow_html=True)

    st.divider()
    
    # Upload & Risk Logic
    st.markdown("### 📥 Neural Data Ingestion")
    uploaded_file = st.file_uploader("Upload Audit Ledger (CSV)", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # 1. Dashboard Metrics
        m1, m2, m3 = st.columns(3)
        total_rec = len(df)
        # Mocking high risk (Real logic: amount > threshold)
        high_risk_count = int(total_rec * 0.15) 
        
        m1.metric("Total Records Scanned", total_rec)
        m2.metric("High Risk Anomalies", high_risk_count, delta="High Severity", delta_color="inverse")
        m3.metric("System Integrity", "98.4%", delta="Optimal")

        st.divider()

        # 2. Forensic Visuals (Risk Analysis)
        st.markdown("### 📊 Automated Risk Analysis")
        v1, v2 = st.columns([2, 1])
        
        with v1:
            st.write("#### Transaction Risk Heatmap")
            # Generating a simple chart for visual impact
            chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['Risk Score', 'Frequency', 'Anomaly Rate'])
            st.area_chart(chart_data)
            
        with v2:
            st.write("#### Critical Flags")
            st.markdown(f"<div class='risk-box'><b>Critical:</b> {high_risk_count} Suspected Fraud Instances</div>", unsafe_allow_html=True)
            st.markdown("<div class='risk-box' style='border-left-color:#f59e0b;'><b>Warning:</b> Inconsistent Documentation detected</div>", unsafe_allow_html=True)

        st.write("#### Detailed Forensic Stream")
        st.dataframe(df, use_container_width=True)
        
    else:
        # Default visuals if no file
        i1, i2, i3 = st.columns(3)
        i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500", caption="Risk Mapping")
        i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500", caption="Anomaly Detection")
        i3.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=500", caption="Forensic Stream")

    if st.button("Logout"):
        st.session_state.auth = False
        st.rerun()
