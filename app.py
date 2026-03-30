import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# 2. Master CSS (Absolute Centering & Compact Styling)
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: white; }
    
    /* CS BRAND LOGO (Top Left Fixed) */
    .brand-logo { 
        position: fixed; top: 30px; left: 30px; font-size: 26px; font-weight: 800; 
        color: #38bdf8; border: 3px solid #38bdf8; padding: 8px 20px; 
        letter-spacing: 5px; background: rgba(56, 189, 248, 0.1); z-index: 999; 
    }

    /* Logic to force everything to Page Middle */
    .main .block-container { 
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 90vh; /* Centering vertically */
    }

    /* Sleek Small Auth Card */
    .auth-card { 
        background: rgba(22, 30, 46, 0.9); 
        padding: 25px 35px; 
        border-radius: 15px; 
        border: 1px solid rgba(255, 255, 255, 0.1); 
        text-align: center; 
        width: 380px; /* Compact Width */
        margin-top: 10px;
    }
    
    /* Small Sleek Text Boxes */
    input {
        background-color: #0b0f19 !important; color: white !important;
        border: 1px solid #1e293b !important; border-radius: 6px !important;
        height: 32px !important; 
        text-align: center;
        font-size: 14px !important;
    }

    /* Blue Button Styling */
    div.stButton > button { 
        background-color: #38bdf8 !important; color: #000 !important; 
        font-weight: bold !important; width: 100%; border-radius: 6px !important; 
        height: 38px; margin-top: 10px;
    }

    /* Remove Streamlit default gap and junk */
    header, footer { visibility: hidden; }
    .stTabs [data-baseweb="tab-list"] { justify-content: center !important; gap: 15px; }
    </style>
    <div class="brand-logo">C S</div>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 3. AUTHENTICATION SCREEN (Middle Aligned) ---
if not st.session_state.auth:
    # Title Section
    st.markdown("<h1 style='text-align: center; margin-bottom: -10px;'>🛡️</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px; margin-bottom: 0px;'>RISKSHIELD AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; font-size: 13px;'>ENTERPRISE ADVISORY PORTAL</p>", unsafe_allow_html=True)
    
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
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2
