import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="CHARVI SRI | RiskShield AI", layout="wide", page_icon="🤖")

# --- Custom Premium Design ---
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; }
    .auth-container {
        background: rgba(255, 255, 255, 0.02);
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #38bdf8;
    }
    .top-left-logo {
        font-size: 22px;
        font-weight: bold;
        color: #38bdf8;
        border: 2px solid #38bdf8;
        padding: 5px 15px;
        letter-spacing: 3px;
    }
    input { background-color: #111 !important; color: #38bdf8 !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- Database Mockup (Session State) ---
if 'user_db' not in st.session_state:
    st.session_state.user_db = {} # {username: password}
if 'auth' not in st.session_state:
    st.session_state.auth = False

# --- AUTHENTICATION FLOW ---
if not st.session_state.auth:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<center><img src='https://cdn-icons-png.flaticon.com/512/11516/11516905.png' width='80'></center>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns([1, 1.5, 1])
    with c2:
        st.markdown('<div class="auth-container">', unsafe_allow_html=True)
        tab1, tab2 = st.tabs(["🔑 LOGIN", "📝 REGISTER"])
        
        with tab2: # Registration Section
            st.markdown("<h3 style='color:#38bdf8;'>Create New Account</h3>", unsafe_allow_html=True)
            reg_user = st.text_input("Choose Identity ID", key="reg_u")
            reg_pass = st.text_input("Create Security Key", type="password", key="reg_p")
            if st.button("CREATE ACCOUNT"):
                if reg_user and reg_pass:
                    st.session_state.user_db[reg_user] = reg_pass
                    st.success("Registration Successful! Now go to Login tab.")
                else:
                    st.warning("Please enter valid details
