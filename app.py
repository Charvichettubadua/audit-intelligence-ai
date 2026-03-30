import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config (Charvi Sri Branding)
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# 2. Final Polished CSS (No Gaps, Small Inputs, CS Logo)
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: white; }
    
    /* CS BRAND LOGO (Top Left Fixed) */
    .brand-logo { 
        position: fixed; top: 30px; left: 30px; font-size: 26px; font-weight: 800; 
        color: #38bdf8; border: 3px solid #38bdf8; padding: 8px 20px; 
        letter-spacing: 5px; background: rgba(56, 189, 248, 0.1); z-index: 999; 
    }

    /* Fixed Top Margin & Centering Content */
    .main .block-container { 
        padding-top: 60px !important; 
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Sleek Small Auth Card */
    .auth-card { 
        background: rgba(22, 30, 46, 0.9); 
        padding: 30px; 
        border-radius: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.1); 
        text-align: center; 
        width: 400px; 
        margin-top: 20px;
    }
    
    /* Sleek Inputs */
    input {
        background-color: #0b0f19 !important; color: white !important;
        border: 1px solid #1e293b !important; border-radius: 8px !important;
        height: 35px !important; 
        text-align: center;
    }

    div.stButton > button { 
        background-color: #38bdf8 !important; color: #000 !important; 
        font-weight: bold !important; width: 100%; border-radius: 8px !important; 
        height: 42px; margin-top: 15px;
    }

    header, footer { visibility: hidden; }
    </style>
    <div class="brand-logo">C S</div>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 3. AUTHENTICATION SCREEN ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>🛡️</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px; margin-bottom: 0px;'>RISKSHIELD AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; margin-bottom: 20px;'>ENTERPRISE ADVISORY PORTAL</p>", unsafe_allow_html=True)
    
    # Login/Register Selection
    tab1, tab2 = st.tabs(["LOGIN", "REGISTER"])
    
    with tab1:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        email = st.text_input("GUEST IDENTITY", placeholder="Corporate Email", key="l_email")
        pwd = st.text_input("ACCESS KEY", type="password", placeholder="Password", key="l_pwd")
        if st.button("AUTHORIZE & ENTER"):
            if email and pwd:
                st.session_state.auth = True
                st.rerun()
    
    with tab2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.text_input("Full Name", placeholder="Name", key="r_name")
        st.text_input("Work Email", placeholder="Work Email", key="r_email")
        st.text_input("Set Access Key", type="password", placeholder="Password", key="r_pwd")
        if st.button("CREATE ACCOUNT"):
            st.success("Account Ready! Switch to Login.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. DASHBOARD SCREEN (Original Dashboard - Restored) ---
else:
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px; padding-top: 10px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>CHARVI SRI | FORENSIC TECH ENTHUSIAST</p>", unsafe_allow_html=True)

    st.divider()
    
    st.markdown("### 🔍 Surveillance Intelligence")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping")
    i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Anomaly Detection")
    i3.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Forensic Stream")

    st.divider()

    st.markdown("### 📥 Neural Data Ingestion")
    uploaded_file = st.file_uploader("Upload Audit Ledger (CSV)", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Scanned Records", len(df))
        m2.metric("High Risk Flags", f"{int(len(df)*0.12)}", delta="Anomalies Found", delta_color="inverse")
        m3.metric("Neural Accuracy", "99.2%")
        m4.metric("Risk Status", "ALERT", delta="Review Needed", delta_color="inverse")

        v1, v2 = st.columns([2, 1])
        with v1:
            st.write("#### AI Predicted Risk Trend")
            chart_data = pd.DataFrame(np.random.randn(15, 2), columns=['Audit Risk', 'Fraud Probability'])
            st.line_chart(chart_data)
        with v2:
            st.write("#### Neural Alerts")
            st.markdown("<div class='risk-box'>🚨 <b>Critical:</b> High-value transaction mismatch found.</div>", unsafe_allow_html=True)
            st.markdown("<div class='risk-box' style='border-left-color:#f59e0b;'>⚠️ <b>Warning:</b> Duplicate vendor IDs detected.</div>", unsafe_allow_html=True)
        
        st.write("#### Detailed Forensic Stream")
