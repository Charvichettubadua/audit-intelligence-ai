import streamlit as st
import requests
import pandas as pd

# Page Configuration
st.set_page_config(page_title="RiskShield AI | Client Portal", page_icon="🛡️", layout="wide")

# Custom CSS for Startup Look
st.markdown("""
    <style>
    .main { background-color: #0d1117; color: white; }
    .stButton>button { width: 100%; background-color: #238636; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

def login_page():
    st.title("🛡️ RiskShield AI")
    st.subheader("Login to your Enterprise Account")
    
    with st.form("login_form"):
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            if email == "admin@riskshield.ai" and password == "admin123": # Temporary check
                st.session_state['logged_in'] = True
                st.success("Welcome back, CEO!")
                st.rerun()
            else:
                st.error("Invalid Credentials")

def registration_page():
    st.title("🚀 Join RiskShield AI")
    st.subheader("Start your 14-day Free Trial")
    
    with st.form("reg_form"):
        name = st.text_input("Full Name")
        org = st.text_input("Organization Name")
        email = st.text_input("Work Email")
        pwd = st.text_input("Set Password", type="password")
        submit = st.form_submit_button("Register Account")
        
        if submit:
            st.success("Account created! Please login.")

def dashboard_page():
    st.sidebar.title("RiskShield Menu")
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()

    st.title("📊 Forensic Audit Portal")
    uploaded_file = st.file_uploader("Upload Transaction Log (CSV)", type="csv")

    if uploaded_file:
        st.info("AI Analysis in progress...")
        # Connecting to our existing FastAPI Backend
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/analyze", files={"file": (uploaded_file.name, uploaded_file.getvalue())})
        
        if response.status_code == 200:
            data = response.json()
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Records", data['total_records'])
            col2.metric("Anomalies", data['suspicious_count'], delta_color="inverse")
            col3.metric("Risk Status", data['risk_level'])
            
            st.success("Audit Completed Successfully!")
        else:
            st.error("Backend Connection Error")

# Main App Logic
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    tab1, tab2 = st.tabs(["Login", "Register"])
    with tab1: login_page()
    with tab2: registration_page()
else:
    dashboard_page()
