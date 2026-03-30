import streamlit as st
import requests
import pandas as pd
import io

# 1. Page Config
st.set_page_config(page_title="CS | RiskShield AI", layout="wide")

# 2. Advanced Professional CSS (Hard Override)
st.markdown("""
    <style>
    /* Force Background and Text Colors */
    .stApp { background-color: #0d1117 !important; color: #c9d1d9 !important; }
    
    /* True Center Alignment - Everything in Middle */
    .main .block-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh; /* Centered in Viewport */
        text-align: center;
        margin: auto;
    }

    /* Professional Floating Brand Logo */
    .brand-logo { 
        position: fixed; top: 25px; left: 25px; font-size: 24px; font-weight: 800; 
        color: #38bdf8; border: 2px solid #38bdf8; padding: 5px 15px; 
        background: rgba(56, 189, 248, 0.1); border-radius: 5px; 
    }

    /* Glassmorphism Card Style (Matching your request) */
    [data-testid="stForm"], .metric-card {
        background: rgba(22, 30, 46, 0.7);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        backdrop-filter: blur(15px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    /* Professional Small Text Boxes (FIXED ERROR) */
    .stTextInput div div input {
        background-color: #0d1117 !important;
        color: white !important;
        border: 1px solid #30363d !important;
        height: 32px !important; /* Smaller Height */
        border-radius: 8px !important;
        width: 100% !important;
        max-width: 350px !important; /* Smaller Width */
        margin: auto;
    }

    /* Centered Tabs Cyan on Dark */
    button[data-baseweb="tab"] {
        margin: auto;
        color: #58a6ff !important; /* Professional Cyan */
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: white !important; /* White for selected */
    }

    /* Primary Blue Buttons (Matching Video) */
    .stButton>button {
        background-color: #0066ff !important;
        color: white !important;
        width: 100% !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        margin-top: 15px;
    }
    .stButton>button:hover { background-color: #005cc5 !important; }

    h1, h2 { color: #00d4ff !important; margin-bottom: 20px; }
    
    header, footer { visibility: hidden; }
    </style>
    <div class="brand-logo">CS</div>
    """, unsafe_allow_html=True)

# 3. Session State
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# --- AUTH FLOW ---
if not st.session_state['logged_in']:
    # Centered Logo and Title
    st.markdown("<h1 style='text-align: center;'>🛡️</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>RiskShield AI</h1>", unsafe_allow_html=True)
    
    # Selection Tabs (Cyan style)
    tab1, tab2 = st.tabs(["PORTAL LOGIN", "CREATE ACCOUNT"])
    
    with tab1:
        with st.form("login_form"):
            st.markdown("<h3 style='text-align: center; color: #8b949e;'>Identity required for full access</h3>", unsafe_allow_html=True)
            email = st.text_input("Work Email")
            pwd = st.text_input("Access Key", type="password")
            submit = st.form_submit_button("AUTHORIZE & ENTER")
            
            if submit:
                # Backend (FastAPI) API Call
                res = requests.post("http://127.0.0.1:8000/login", data={"email": email, "password": pwd}).json()
                if res['status'] == 'success':
                    st.session_state['logged_in'] = True
                    st.session_state['user'] = res['user']
                    st.rerun()
                else: st.error("Access Denied: Invalid Credentials")

    with tab2:
        with st.form("reg_form"):
            st.markdown("<h3 style='text-align: center; color: #8b949e;'>Deloitte Manager Identity</h3>", unsafe_allow_html=True)
            name = st.text_input("Full Name")
            re
