import streamlit as st
import pandas as pd
import numpy as np
import requests

# --- 1. Page Config (As per your design) ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# --- 2. Premium CSS (Retaining your style + adding centering for Auth) ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: white; }
    .brand-logo { position: fixed; top: 30px; left: 30px; font-size: 26px; font-weight: 800; color: #38bdf8; border: 3px solid #38bdf8; padding: 8px 20px; letter-spacing: 5px; background: rgba(56, 189, 248, 0.1); z-index: 999; }
    
    /* Auth Card Styling */
    .auth-card { 
        background: #161e2e; 
        padding: 40px; 
        border-radius: 20px; 
        border: 1px solid #1e293b; 
        text-align: center; 
        margin: auto;
        max-width: 450px;
    }
    
    div.stButton > button { background-color: #38bdf8 !important; color: #000 !important; font-weight: bold !important; width: 100%; border-radius: 8px !important; }
    .risk-box { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #ef4444; margin-bottom: 10px; font-size: 14px; }
    .about-section { background: rgba(56, 189, 248, 0.05); padding: 30px; border-radius: 15px; border: 1px solid #38bdf8; margin-top: 50px; }
    
    /* Centering Tabs */
    button[data-baseweb="tab"] { margin: auto !important; color: #8b949e !important; }
    button[data-baseweb="tab"][aria-selected="true"] { color: #38bdf8 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. Session State for Auth Flow ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 4. AUTHENTICATION SCREEN (Login & Register Added) ---
if not st.session_state.auth:
    # Adding CS branding even on login page
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px; margin-top: 50px;'>🛡️ RISKSHIELD AI</h1>", unsafe_allow_html=True)
    
    # Selection for Login or Register
    tab1, tab2 = st.tabs(["PORTAL LOGIN", "CREATE ACCOUNT"])
    
    with tab1:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.markdown("### Secure Access")
        login_email = st.text_input("GUEST IDENTITY", placeholder="Corporate Email")
        login_pwd = st.text_input("ACCESS KEY", type="password", placeholder="••••••••")
        if st.button("AUTHORIZE & ENTER"):
            # Simulation: In POC, any input works, or you can link to FastAPI
            if login_email and login_pwd:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Please provide credentials")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.markdown("### Register Manager")
        st.text_input("Full Name")
        st.text_input("Work Email")
        st.text_input("Organization")
        st.text_input("Set Password", type="password")
        if st.button("INITIALIZE ACCOUNT"):
            st.success("Account Ready! Please switch to Login tab.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. DASHBOARD SCREEN (Your Original Code - Untouched) ---
else:
    # Branding Header
    st.markdown('<div class="brand-logo">C S</div>', unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>CHARVI SRI | FORENSIC TECH ENTHUSIAST</p>", unsafe_allow_html=True)

    st.divider()
    
    # 1. ALWAYS VISIBLE IMAGES
    st.markdown("### 🔍 Surveillance Intelligence")
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping")
    i2.image("
