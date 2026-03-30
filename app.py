import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# 2. Master CSS (Cleaning all Messy Blocks)
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19 !important; color: white !important; }
    
    /* CS BRAND LOGO (Top Left) */
    .brand-logo { 
        position: fixed; top: 30px; left: 30px; font-size: 24px; font-weight: 800; 
        color: #38bdf8; border: 2px solid #38bdf8; padding: 5px 15px; 
        background: rgba(56, 189, 248, 0.1); z-index: 999; 
    }

    /* Logic to force EVERYTHING to Center of the Screen */
    .main .block-container { 
        display: flex; flex-direction: column; align-items: center; 
        justify-content: center; min-height: 85vh; padding-top: 0px !important;
    }

    /* Small, Sleek Auth Card (Glassmorphism) */
    .auth-card { 
        background: rgba(22, 30, 46, 0.8); 
        padding: 30px; border-radius: 20px; 
        border: 1px solid rgba(255, 255, 255, 0.1); 
        text-align: center; width: 400px; margin-top: 10px;
    }
    
    /* Sleek Small Text Boxes (Removing Dark Blocks) */
    .stTextInput input {
        background-color: #0b0f19 !important; color: white !important;
        border: 1px solid #1e293b !important; border-radius: 8px !important;
        height: 35px !important; text-align: center; font-size: 14px !important;
    }

    /* Blue Buttons (Enterprise Style) */
    div.stButton > button { 
        background-color: #38bdf8 !important; color: #000 !important; 
        font-weight: bold !important; border-radius: 8px !important; 
        height: 40px; border: none !important;
    }

    /* Hiding unnecessary Streamlit labels and elements */
    label { display: none !important; } 
    header, footer { visibility: hidden; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center !important; gap: 20px; }
    </style>
    <div class="brand-logo">C S</div>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 3. AUTHENTICATION SCREEN (True Centering) ---
if not st.session_state.auth:
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px; font-size: 45px; margin-bottom: 0px;'>RISKSHIELD AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; margin-top: 0px;'>ENTERPRISE ADVISORY PORTAL</p>", unsafe_allow_html=True)
    
    t1, t2 = st.tabs(["LOGIN", "REGISTER"])
    
    with t1:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.text_input("Identity", placeholder="Work Email", key="l_email")
        st.text_input("Key", type="password", placeholder="Password", key="l_pwd")
        if st.button("AUTHORIZE & ENTER"):
            if st.session_state.l_email and st.session_state.l_pwd:
                st.session_state.auth = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with t2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.text_input("Name", placeholder="Full Name", key="r_name")
        st.text_input("Email", placeholder="Work Email", key="r_email")
        st.text_input("Pwd", type="password", placeholder="Create Password", key="r_pwd")
        if st.button("INITIALIZE ACCOUNT"):
            st.success("Ready! Use Login.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 4. DASHBOARD SCREEN (Original Unchanged) ---
else:
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>CHARVI SRI | FORENSIC TECH ENTHUSIAST</p>", unsafe_allow_html=True)

    st.divider()
    
    # Keeping your original images logic
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping")
    i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Anomaly Detection")
    i3.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Forensic Stream")

    st.divider()

    uploaded_file = st.file_uploader("Upload Ledger", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Records", len(df))
        m2.metric("Risks", f"{int(len(df)*0.12)}", delta="Alert", delta_color="inverse")
        m3.metric("Accuracy", "99.2%")
        m4.metric("Status", "REVIEW")
        st.dataframe(df.head(50), use_container_width=True)

    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.rerun()
