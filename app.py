import streamlit as st
import pandas as pd
import numpy as np

# --- 1. Page Config (Charvi Sri Branding) ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# --- 2. Master CSS (Fixed Spacing & No White Blocks) ---
st.markdown("""
    <style>
    /* Full Dark Mode */
    .stApp { background-color: #0b0f19; color: white; }
    
    /* CS BRAND LOGO (Top Left Fixed) */
    .brand-logo { 
        position: fixed; top: 30px; left: 30px; font-size: 26px; font-weight: 800; 
        color: #38bdf8; border: 3px solid #38bdf8; padding: 8px 20px; 
        letter-spacing: 5px; background: rgba(56, 189, 248, 0.1); z-index: 999; 
    }

    /* Auth Card Styling */
    .auth-card { background: #161e2e; padding: 40px; border-radius: 20px; border: 1px solid #1e293b; text-align: center; margin: auto; max-width: 450px; }
    
    div.stButton > button { background-color: #38bdf8 !important; color: #000 !important; font-weight: bold !important; width: 100%; border-radius: 8px !important; }
    .risk-box { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #ef4444; margin-bottom: 10px; font-size: 14px; }
    .about-section { background: rgba(56, 189, 248, 0.05); padding: 30px; border-radius: 15px; border: 1px solid #38bdf8; margin-top: 50px; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 3. CS BRAND LOGO (Always Visible) ---
st.markdown('<div class="brand-logo">C S</div>', unsafe_allow_html=True)

# --- 4. AUTHENTICATION SCREEN ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>🛡️ RISKSHIELD AI</h1>", unsafe_allow_html=True)
        
        choice = st.radio("Access Portal", ["Login", "Register"], horizontal=True)
        
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        if choice == "Login":
            email = st.text_input("GUEST IDENTITY", placeholder="Work Email", key="l_email")
            pwd = st.text_input("ACCESS KEY", type="password", placeholder="••••••••", key="l_pwd")
            if st.button("AUTHORIZE & ENTER"):
                if email and pwd:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Please enter credentials")
        else:
            st.text_input("Full Name", key="r_name")
            st.text_input("Work Email", key="r_email")
            st.text_input("Set Password", type="password", key="r_pwd")
            if st.button("INITIALIZE ACCOUNT"):
                st.success("Account Ready! Switch to Login.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. DASHBOARD SCREEN (Original Design Fixed) ---
else:
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>COMMAND CENTER
