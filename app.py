import streamlit as st
import pandas as pd
import numpy as np

# --- 1. Page Config (Charvi Sri Branding) ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# --- 2. Master CSS (Fixed Spacing, Centering & White Block) ---
st.markdown("""
    <style>
    /* Full Dark Mode - No White Blocks */
    .stApp { background-color: #0b0f19; color: white; margin-top: -50px; }
    
    /* CS BRAND LOGO (Top Left Fixed) */
    .brand-logo { 
        position: fixed; top: 30px; left: 30px; font-size: 26px; font-weight: 800; 
        color: #38bdf8; border: 3px solid #38bdf8; padding: 8px 20px; 
        letter-spacing: 5px; background: rgba(56, 189, 248, 0.1); z-index: 999; 
    }

    /* Fixed Top Margin for Both Screens */
    .main .block-container { padding-top: 120px !important; }

    /* Auth Card Styling */
    .auth-card { background: #161e2e; padding: 40px; border-radius: 20px; border: 1px solid #1e293b; text-align: center; margin: auto; max-width: 450px; }
    
    div.stButton > button { background-color: #38bdf8 !important; color: #000 !important; font-weight: bold !important; width: 100%; border-radius: 8px !important; }
    .risk-box { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #ef4444; margin-bottom: 10px; font-size: 14px; }
    .about-section { background: rgba(56, 189, 248, 0.05); padding: 30px; border-radius: 15px; border: 1px solid #38bdf8; margin-top: 50px; }
    
    /* Centering Tabs */
    button[data-baseweb="tab"] { margin: auto !important; color: #8b949e !important; }
    button[data-baseweb="tab"][aria-selected="true"] { color: #38bdf8 !important; }
    </style>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 3. CS BRAND LOGO (Always Visible) ---
st.markdown('<div class="brand-logo">C S</div>', unsafe_allow_html=True)

# --- 4. AUTHENTICATION SCREEN ---
if not st.session_state.auth:
    # Small fix for centering logo on login page
    c1, c2, c3 = st.columns([1, 1.2, 1])
    with c2:
        st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>🛡️ RISKSHIELD AI</h1>", unsafe_allow_html=True)
    
    # Simple Tabs for Auth
    choice = st.radio("Access Portal", ["Login", "Register"], horizontal=True)
    
    with st.container():
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        if choice == "Login":
            st.markdown("### Portal Access")
            login_email = st.text_input("GUEST IDENTITY", placeholder="Work Email", key="l_email")
            login_pwd = st.text_input("ACCESS KEY", type="password", placeholder="••••••••", key="l_pwd")
            if st.button("AUTHORIZE & ENTER"):
                # Simulation for demo
                if login_email and login_pwd:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Please provide credentials")
        else:
            st.markdown("### Request Access")
            st.text_input("Full Name", key="r_name")
            st.text_input("Work Email", key="r_email")
            st.text_input("Set Password", type="password", key="r_pwd")
            if st.button("INITIALIZE ACCOUNT"):
                st.success("Account Ready! Switch to Login tab.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. DASHBOARD SCREEN (Your Original Design) ---
else:
