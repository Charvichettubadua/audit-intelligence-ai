import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# --- Premium Executive CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: white; font-family: 'Segoe UI', sans-serif; }
    
    /* CS Top Left Logo */
    .brand-logo {
        position: fixed;
        top: 30px;
        left: 30px;
        font-size: 26px;
        font-weight: 800;
        color: #38bdf8;
        border: 3px solid #38bdf8;
        padding: 8px 20px;
        letter-spacing: 5px;
        background: rgba(56, 189, 248, 0.1);
        z-index: 999;
    }

    /* Auth Card Styling */
    .auth-card {
        background: #161e2e;
        padding: 40px;
        border-radius: 20px;
        border: 1px solid #1e293b;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        text-align: center;
        margin-top: 50px;
    }

    /* Black Hyperlink Style for Buttons & Signout */
    div.stButton > button {
        background-color: #38bdf8 !important;
        color: #000000 !important; /* Pure Black Text */
        font-weight: bold !important;
        border-radius: 8px !important;
        width: 100%;
        border: none !important;
        height: 45px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .signout-link button {
        background: none !important;
        color: #000000 !important;
        text-decoration: underline !important;
        width: auto !important;
        font-size: 14px !important;
    }

    /* File Uploader Style */
    .stFileUploader label {
        color: #000000 !important;
        background-color: #38bdf8;
        padding: 10px;
        border-radius: 5px;
        font-weight: bold;
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Session State ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- AUTHENTICATION SCREEN ---
if not st.session_state.auth:
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        # Professional Shield Logo
        st.markdown("# 🛡️")
        st.markdown("<h2 style='color:#38bdf8; margin-bottom:0;'>RISKSHIELD AI</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#64748b;'>EXECUTIVE FORENSIC PORTAL</p>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        user_id = st.text_input("IDENTITY ID", placeholder="Enter ID...")
        secure_key = st.text_input("SECURE KEY", type="password", placeholder="Enter Key...")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("AUTHORIZE & ENTER"):
            if user_id.lower() == "charvi" and secure_key == "2026":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("ACCESS DENIED: INVALID CREDENTIALS")
        
        st.markdown("<p style='font-size:12px; color:#475569; margin-top:20px;'>SECURED BY CHARVI SRI COMMAND</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    # Top Bar
    st.markdown('<div class="brand-logo">C S</div>', unsafe_allow_html=True)
    
    t1, t2, t3 = st.columns([1, 3, 1])
    with t2:
        st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 10px; font-size: 50px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 18px;'>CHARVI SRI | SENIOR FORENSIC ANALYST</p>", unsafe_allow_html=True)
    with t3:
        st.markdown('<div class="signout-link">', unsafe_allow_html=True)
        if st.button("Log Out Session"):
            st.session_state.auth = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Images Section (Professional Forensic Visuals)
    st.markdown("### 🔍 Surveillance Intelligence")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=500", caption="Neural Risk Analysis")
    i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500", caption="Financial Anomaly Detection")
    i3.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=500", caption="Cyber Forensic Stream")

    st.divider()
    
    # Data Upload
    st.markdown("### 📥 Neural Data Ingestion")
    uploaded_file = st.file_uploader("Upload Audit Ledger (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.success("Data Stream Authenticated.")
        st.dataframe(df.head(20), use_container_width=True)
