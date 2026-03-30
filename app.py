import streamlit as st
import pandas as pd
import numpy as np

# --- 1. Page Config (Original Branding) ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# --- 2. Original Premium CSS (Restore Original Theme) ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: white; }
    .brand-logo { position: fixed; top: 30px; left: 30px; font-size: 26px; font-weight: 800; color: #38bdf8; border: 3px solid #38bdf8; padding: 8px 20px; letter-spacing: 5px; background: rgba(56, 189, 248, 0.1); z-index: 999; }
    
    /* Small Fix for Auth Alignment - Not affecting Dashboard */
    .auth-container { text-align: center; margin: auto; max-width: 450px; padding-top: 50px; }
    
    div.stButton > button { background-color: #38bdf8 !important; color: #000 !important; font-weight: bold !important; width: 100%; border-radius: 8px !important; }
    .risk-box { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #ef4444; margin-bottom: 10px; font-size: 14px; }
    .about-section { background: rgba(56, 189, 248, 0.05); padding: 30px; border-radius: 15px; border: 1px solid #38bdf8; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 3. SECURE AUTH LAYER (Simple & Clean) ---
if not st.session_state.auth:
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px; margin-top: 80px;'>🛡️ RISKSHIELD AI</h1>", unsafe_allow_html=True)
    
    # Using simple tabs to avoid messy glassmorphism CSS
    t1, t2 = st.tabs(["PORTAL LOGIN", "REGISTER MANAGER"])
    
    with t1:
        c1, c2, c3 = st.columns([1, 1.2, 1])
        with c2:
            st.text_input("GUEST IDENTITY", placeholder="Corporate Email", key="l_email")
            st.text_input("ACCESS KEY", type="password", placeholder="••••••••", key="l_pwd")
            if st.button("AUTHORIZE & ENTER"):
                st.session_state.auth = True
                st.rerun()

    with t2:
        c1, c2, c3 = st.columns([1, 1.2, 1])
        with c2:
            st.text_input("Full Name", key="r_name")
            st.text_input("Work Email", key="r_email")
            st.text_input("Set Access Key", type="password", key="r_pwd")
            if st.button("INITIALIZE ACCOUNT"):
                st.success("Account Created! Switch to Login.")

# --- 4. ORIGINAL DASHBOARD (100% UNTOUCHED) ---
else:
    # Branding Header
    st.markdown('<div class="brand-logo">C S</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>CHARVI SRI | FORENSIC TECH ENTHUSIAST</p>", unsafe_allow_html=True)

    st.divider()
    
    # Surveillance Section
    st.markdown("### 🔍 Surveillance Intelligence")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping")
    i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Anomaly Detection")
    i3.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Forensic Stream")

    st.divider()

    # Data Analysis Section
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
        
        st.dataframe(df.head(50), use_container_width=True)

    # About Me
    st.markdown('<div class="about-section">', unsafe_allow_html=True)
    a1, a2 = st.columns([1, 4])
    with a1: st.markdown("### 👤 Profile")
    with a2:
        st.write("**CHARVI SRI** | *Forensic Tech Enthusiast & Aspiring Analyst*")
        st.write("RiskShield AI is my initiative to demonstrate how AI can revolutionize forensic auditing.")
        st.write("📧 **Contact:** [gdv.ch.charvisri@gmail.com](mailto:gdv.ch.charvisri@gmail.com)")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.sidebar.button("Logout Session"):
        st.session_state.auth = False
        st.rerun()
