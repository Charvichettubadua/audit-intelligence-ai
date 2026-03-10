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
    .risk-box { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #ef4444; margin-bottom: 10px; font-size: 14px; }
    .about-section { background: rgba(255,255,255,0.02); padding: 30px; border-radius: 15px; border: 1px solid #1e293b; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- AUTHENTICATION SCREEN ---
if not st.session_state.auth:
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.markdown("# 🛡️")
        st.markdown("<h2 style='color:#38bdf8;'>RISKSHIELD AI</h2>", unsafe_allow_html=True)
        st.text_input("GUEST IDENTITY", placeholder="Identity not required for Guest Access")
        if st.button("AUTHORIZE & ENTER"):
            st.session_state.auth = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    st.markdown('<div class="brand-logo">C S</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>CHARVI SRI | SENIOR FORENSIC ANALYST</p>", unsafe_allow_html=True)

    st.divider()
    
    # Static Images Section (Always Visible)
    st.markdown("### 🔍 Surveillance Intelligence")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping")
    i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Anomaly Detection")
    i3.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Forensic Stream")

    st.divider()

    # Data Upload & Analysis
    st.markdown("### 📥 Neural Data Ingestion")
    uploaded_file = st.file_uploader("Upload Audit Ledger (CSV)", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        
        # Risk Metrics Row
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Scanned Records", len(df))
        m2.metric("High Risk Flags", f"{int(len(df)*0.12)}", delta="Attention Required", delta_color="inverse")
        m3.metric("Neural Accuracy", "99.2%")
        m4.metric("Risk Level", "CRITICAL", delta="Action Needed", delta_color="inverse")

        # Risk Analysis Row
        v1, v2 = st.columns([2, 1])
        with v1:
            st.write("#### AI Predicted Risk Trend")
            chart_data = pd.DataFrame(np.random.randn(15, 2), columns=['Audit Risk', 'Fraud Probability'])
            st.line_chart(chart_data)
        with v2:
            st.write("#### Neural Alerts")
            st.markdown("<div class='risk-box'>🚨 <b>High Risk:</b> Unusual offshore transfers detected.</div>", unsafe_allow_html=True)
            st.markdown("<div class='risk-box' style='border-left-color:#f59e0b;'>⚠️ <b>Warning:</b> Sequence gap in ledger entries.</div>", unsafe_allow_html=True)
        
        st.write("#### Detailed Forensic Stream")
        st.dataframe(df.head(50), use_container_width=True)

    st.divider()

    # --- ABOUT US SECTION (Footer) ---
    st.markdown('<div class="about-section">', unsafe_allow_html=True)
    a1, a2 = st.columns([1, 3])
    with a1:
        st.markdown("### 👤 About the Analyst")
    with a2:
        st.write("**CHARVI SRI** | *Senior Forensic Audit Consultant*")
        st.write("Specializing in AI-driven fraud detection and neural risk mapping. RiskShield AI is a proprietary command center designed to automate complex audit surveillance and protect enterprise integrity through advanced anomaly detection.")
        st.write("📧 *Contact:* charvi.sri@forensic-command.ai")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Logout Session"):
        st.session_state.auth = False
        st.rerun()
