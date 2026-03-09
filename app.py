import streamlit as st
import pandas as pd
import plotly.express as px
import os

# --- Page Config ---
st.set_page_config(page_title="RiskShield AI | Secure Portal", layout="wide", page_icon="🛡️")

# --- Custom CSS for Professional Look ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #004b91; color: white; }
    .login-box { padding: 2rem; border-radius: 10px; background-color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- Session State Management ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- Credentials (Ikkada marchuko Chintu) ---
USER_NAME = "admin"
PASSWORD = "deloitte_audit"

# --- Login UI ---
def login_screen():
    cols = st.columns([1, 2, 1])
    with cols[1]:
        st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=100)
        st.title("🛡️ RiskShield AI Portal")
        st.subheader("Enterprise Audit Intelligence")
        
        with st.container():
            username = st.text_input("User ID")
            password = st.text_input("Access Key", type="password")
            
            if st.button("Authenticate"):
                if username == USER_NAME and password == PASSWORD:
                    st.session_state.logged_in = True
                    st.success("Access Granted! Loading Audit Engine...")
                    st.rerun()
                else:
                    st.error("Authentication Failed. Please check credentials.")

# --- Main Dashboard ---
def main_dashboard():
    st.sidebar.title("🛡️ RiskShield AI")
    st.sidebar.info(f"User: {USER_NAME} (Active)")
    if st.sidebar.button("Secure Logout"):
        st.session_state.logged_in = False
        st.rerun()

    st.title("📊 Forensic Audit Dashboard")
    st.write("Welcome back! Please upload the transaction data for AI analysis.")
    
    uploaded_file = st.file_uploader("Choose Audit CSV File", type="csv")
    if uploaded_file is not None:
        # Ikkada nee patha agent.py logic and engine ni call cheyachu
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:", df.head())
        st.success("File Processed. AI Analysis ready.")

# --- App Logic ---
if not st.session_state.logged_in:
    login_screen()
else:
    main_dashboard()
