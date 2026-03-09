import streamlit as st
import pandas as pd
import time

# --- Ultra-Premium Config ---
st.set_page_config(page_title="CHARVI SRI | AI AUDIT", layout="centered", page_icon="✨")

# --- Luxury Aesthetic CSS ---
st.markdown("""
    <style>
    /* Background override to Deep Obsidian */
    .stApp {
        background: #050505 !important;
        color: #ffffff;
    }
    
    /* Login Frame */
    .login-frame {
        background: linear-gradient(145deg, #111111, #000000);
        padding: 60px;
        border-radius: 2px;
        border-top: 4px solid #4facfe;
        box-shadow: 0 50px 100px rgba(0,0,0,0.9);
        text-align: center;
    }

    /* CS Signature Logo */
    .cs-logo {
        font-family: 'Serif';
        font-size: 60px;
        font-weight: 200;
        background: -webkit-linear-gradient(#ffffff, #4facfe);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
        letter-spacing: 5px;
    }

    /* Elegant Text Inputs */
    .stTextInput>div>div>input {
        background-color: #000000 !important;
        color: #4facfe !important;
        border: 1px solid #222 !important;
        border-radius: 0px !important;
        border-bottom: 1px solid #4facfe !important;
        height: 45px;
    }

    /* High-Fashion Button */
    .stButton>button {
        background: transparent !important;
        color: #4facfe !important;
        border: 1px solid #4facfe !important;
        border-radius: 0px !important;
        font-weight: 300 !important;
        letter-spacing: 3px;
        text-transform: uppercase;
        width: 100%;
        margin-top: 20px;
        transition: 0.4s ease;
    }
    .stButton>button:hover {
        background: #4facfe !important;
        color: black !important;
        box-shadow: 0 0 20px #4facfe;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- Credentials ---
CRED_USER = "charvisri"
CRED_PASS = "charvi@2026"

if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# --- LOGIN SCREEN ---
if not st.session_state.authenticated:
    st.markdown('<div class="login-frame">', unsafe_allow_html=True)
    st.markdown('<div class="cs-logo">CS</div>', unsafe_allow_html=True)
    st.markdown("<h3 style='font-weight: 100; color: #888;'>CHARVI SRI EXECUTIVE PORTAL</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 12px; color: #444; margin-bottom: 40px;'>ENTERPRISE FORENSIC INTELLIGENCE</p>", unsafe_allow_html=True)
    
    user = st.text_input("IDENTITY", placeholder="USER ID")
    pw = st.text_input("KEY", type="password", placeholder="ACCESS KEY")
    
    if st.button("AUTHORIZE"):
        if user == CRED_USER and pw == CRED_PASS:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("ACCESS DENIED")
    st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
else:
    st.markdown(f"<h1 style='text-align: center; letter-spacing: 10px; font-weight: 200;'>CHARVI <span style='color:#4facfe'>SRI</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #555;'>FORENSIC AUDIT COMMAND CENTER</p>", unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns(3)
    col1.metric("AUDITOR", "CHARVI SRI")
    col2.metric("SYSTEM", "SECURE")
    col3.metric("AI CORE", "ENABLED")

    st.markdown("<br><br>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader("INGEST DATASET", type="csv")
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, use_container_width=True)
        st.success("AUTHENTICATED DATA LOADED.")
