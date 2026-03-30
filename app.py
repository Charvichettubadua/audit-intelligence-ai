import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Config
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# 2. Hard-Coded CSS for Perfect Alignment
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19 !important; color: white !important; }
    
    /* CS BRAND LOGO (Top Left) */
    .brand-logo { 
        position: fixed; top: 30px; left: 30px; font-size: 24px; font-weight: 800; 
        color: #38bdf8; border: 2px solid #38bdf8; padding: 5px 15px; 
        background: rgba(56, 189, 248, 0.1); z-index: 999; 
    }

    /* Centering Everything in Viewport */
    .main .block-container { 
        display: flex; flex-direction: column; align-items: center; 
        justify-content: center; min-height: 80vh; 
    }

    /* Sleek Card - Equal Width to Tabs */
    .auth-card { 
        background: rgba(22, 30, 46, 0.8); 
        padding: 30px; border-radius: 0px 0px 15px 15px; 
        border: 1px solid rgba(255, 255, 255, 0.1); 
        text-align: center; width: 450px; margin-top: -1px;
    }
    
    /* Text Boxes - Professional & Centered */
    .stTextInput input {
        background-color: #0b0f19 !important; color: white !important;
        border: 1px solid #1e293b !important; border-radius: 8px !important;
        height: 38px !important; text-align: center; font-size: 14px !important;
    }

    /* Blue Button */
    div.stButton > button { 
        background-color: #38bdf8 !important; color: #000 !important; 
        font-weight: bold !important; border-radius: 8px !important; 
        height: 42px; border: none !important; margin-top: 10px;
    }

    /* Tab Styling - Equal Width to Card */
    .stTabs [data-baseweb="tab-list"] { 
        justify-content: center !important; gap: 0px; width: 450px;
        background: rgba(22, 30, 46, 0.5); border-radius: 15px 15px 0px 0px;
    }
    .stTabs [data-baseweb="tab"] { width: 225px !important; }

    label { display: none !important; } 
    header, footer { visibility: hidden; }
    </style>
    <div class="brand-logo">C S</div>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- 3. AUTHENTICATION SCREEN ---
if not st.session_state.auth:
    # 🛡️ SHIELD LOGO RE-ADDED HERE
    st.markdown("<h1 style='text-align: center; font-size: 60px; margin-bottom: 0px;'>🛡️</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px; font-size: 40px; margin-top: 0px;'>RISKSHIELD AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; margin-top: -10px;'>ENTERPRISE ADVISORY PORTAL</p>", unsafe_allow_html=True)
    
    # Tabs & Card Alignment
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

# --- 4. DASHBOARD SCREEN ---
else:
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.divider()
    
    # Rest of your dashboard logic...
    i1, i2, i3 = st.columns(3)
    i1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping")
    i2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Anomaly Detection")
    i3.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Forensic Stream")

    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.rerun()
