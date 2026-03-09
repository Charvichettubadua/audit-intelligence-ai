import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Clean Professional CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    
    /* CS Top Left Logo */
    .top-left-logo {
        position: fixed;
        top: 50px;
        left: 20px;
        font-size: 22px;
        font-weight: bold;
        color: #38bdf8;
        border: 2px solid #38bdf8;
        padding: 5px 15px;
        letter-spacing: 5px;
        z-index: 999;
    }

    /* Auth Card */
    .auth-container {
        background: rgba(255, 255, 255, 0.02);
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #38bdf8;
        text-align: center;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] { color: #888; }
    .stTabs [data-baseweb="tab-highlight"] { background-color: #38bdf8; }
    </style>
    """, unsafe_allow_html=True)

# --- Initializing User Database ---
if 'user_db' not in st.session_state:
    st.session_state.user_db = {} 
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- AUTHENTICATION PAGE ---
if not st.session_state.auth:
    st.markdown("<br><br>", unsafe_allow_html=True)
    # Android Robot Logo Center
    st.markdown("<center><img src='https://cdn-icons-png.flaticon.com/512/11516/11516905.png' width='100'></center>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        st.markdown("<h2 style='color:#38bdf8; letter-spacing:2px;'>RISKSHIELD PORTAL</h2>", unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["🔒 LOGIN", "📝 REGISTER"])
        
        with tab2:
            st.write("New Auditor Registration")
            reg_u = st.text_input("Create Identity ID", key="reg_u")
            reg_p = st.text_input("Create Security Key", type="password", key="reg_p")
            if st.button("REGISTER ACCOUNT"):
                if reg_u and reg_p:
                    st.session_state.user_db[reg_u] = reg_p
                    st.success("Account Created! Please switch to Login tab.")
                else:
                    st.warning("Fields cannot be empty.")

        with tab1:
            st.write("Identity Verification")
            log_u = st.text_input("Identity ID", key="log_u")
            log_p = st.text_input("Security Key", type="password", key="log_p")
            if st.button("VERIFY & ENTER"):
                if log_u in st.session_state.user_db and st.session_state.user_db[log_u] == log_p:
                    st.session_state.auth = True
                    st.rerun()
                else:
                    st.error("Authentication Pending: Identity mismatch.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- EXECUTIVE DASHBOARD ---
else:
    # Header: CS Logo Top Left
    st.markdown('<div class="top-left-logo">C S</div>', unsafe_allow_html=True)
    
    t1, t2, t3 = st.columns([1, 2, 1])
    with t2:
