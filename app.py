import streamlit as st
import pandas as pd
import numpy as np

# 1. Page Configuration
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🛡️")

# 2. Hard-Coded CSS for Perfect Rectangle Card & Centering
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19 !important; color: white !important; }
    
    /* CS BRAND LOGO (Top Left) */
    .brand-logo { 
        position: fixed; top: 30px; left: 30px; font-size: 26px; font-weight: 800; 
        color: #38bdf8; border: 3px solid #38bdf8; padding: 8px 20px; 
        letter-spacing: 5px; background: rgba(56, 189, 248, 0.1); z-index: 999; 
    }

    /* Force Centering in the Middle of Screen */
    .main .block-container { 
        display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 85vh; padding-top: 0px !important;
    }

    /* Account Access Card (Screenshot 125 Exact Match) */
    .auth-card-final { 
        background-color: #161e2e; 
        padding: 40px; 
        border-radius: 20px; 
        border: 1px solid #1e293b; 
        text-align: center; 
        width: 440px; /* Force Narrow Width */
        margin: auto;
    }
    
    /* Centered Labels Above Boxes */
    .input-header { color: #8b949e; font-size: 14px; margin-bottom: 5px; text-align: left; width: 100%; display: block; }

    /* Compact Text Boxes */
    .stTextInput input {
        background-color: #0b0f19 !important; color: white !important;
        border: 1px solid #1e293b !important; border-radius: 8px !important;
        height: 38px !important; text-align: left !important; padding-left: 15px !important;
    }

    /* Enterprise Blue Button */
    div.stButton > button { 
        background-color: #38bdf8 !important; color: #000000 !important; 
        font-weight: bold !important; width: 100%; border-radius: 8px !important; 
        height: 45px; border: none !important; margin-top: 15px;
    }

    /* Tab Alignment to Card Width */
    .stTabs [data-baseweb="tab-list"] { 
        justify-content: center !important; gap: 0px; width: 440px; border-bottom: none !important;
    }
    .stTabs [data-baseweb="tab"] { width: 220px !important; font-weight: bold !important; color: #8b949e !important; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { color: #38bdf8 !important; border-bottom: 2px solid #38bdf8 !important; }

    header, footer { visibility: hidden; }
    label { display: none !important; }
    </style>
    <div class="brand-logo">C S</div>
    """, unsafe_allow_html=True)

if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- UI FLOW ---
if not st.session_state.auth:
    # Title Section (Shield + Single Line)
    st.markdown("<h1 style='text-align: center; font-size: 60px; margin-bottom: 0px;'>🛡️</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px; font-size: 45px; margin-top: 0px;'>RiskShield AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #64748b; margin-top: -15px;'>ENTERPRISE ADVISORY PORTAL</p>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Login Portal", "Register Account"])
    
    with tab1:
        st.markdown('<div class="auth-card-final">', unsafe_allow_html=True)
        st.markdown("<h2 style='color: white; margin-bottom: 25px; font-size: 24px;'>Account Access</h2>", unsafe_allow_html=True)
        
        st.markdown("<p class='input-header'>Enter Work Email</p>", unsafe_allow_html=True)
        email = st.text_input("Email", placeholder="Email", key="login_email_final")
        
        st.markdown("<p class='input-header' style='margin-top: 15px;'>Enter Password</p>", unsafe_allow_html=True)
        pwd = st.text_input("Password", type="password", placeholder="Password", key="login_pwd_final")
        
        if st.button("Login to Enterprise", key="login_btn_final"):
            if email and pwd:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Access Denied")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="auth-card-final">', unsafe_allow_html=True)
        st.markdown("<h2 style='color: white; margin-bottom: 25px; font-size: 24px;'>Register Identity</h2>", unsafe_allow_html=True)
        st.text_input("Full Name", placeholder="Full Name", key="reg_name_final")
        st.text_input("Work Email", placeholder="Work Email", key="reg_email_final")
        st.text_input("Set Access Key", type="password", placeholder="Password", key="reg_pwd_final")
        if st.button("CREATE ACCOUNT", key="reg_btn_final"):
            st.success("Ready! Switch to Login Portal.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    st.markdown("<h1 style='text-align: center; color: #38bdf8; letter-spacing: 5px;'>COMMAND CENTER</h1>", unsafe_allow_html=True)
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    col1.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=400", caption="Neural Risk Mapping")
    col2.image("https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=400", caption="Anomaly Detection")
    col3.image("https://images.unsplash.com/photo-1563986768609-322da13575f3?w=400", caption="Forensic Stream")

    if st.sidebar.button("Logout"):
        st.session_state.auth = False
        st.rerun()
