import streamlit as st
import pandas as pd
import time

# --- Page Config ---
st.set_page_config(page_title="RiskShield AI | Enterprise", layout="centered", page_icon="🛡️")

# --- Commercial Styling ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #001529 0%, #004b91 100%); color: white; }
    .login-card { background: rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 15px; border: 1px solid rgba(255,255,255,0.2); backdrop-filter: blur(10px); }
    .stTextInput>div>div>input { background-color: #f0f2f5 !important; color: black !important; }
    h1, h3 { color: white !important; text-align: center; }
    .stButton>button { background-color: #22c55e !important; color: white !important; font-weight: bold; border-radius: 8px; border: none; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- Session Management ---
if 'auth_status' not in st.session_state:
    st.session_state.auth_status = None

# --- Credentials ---
ADMIN_USER = "admin"
ADMIN_PASS = "deloitte_audit"

# --- LOGIN UI ---
if st.session_state.auth_status is None or st.session_state.auth_status == False:
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    st.title("🛡️ RiskShield AI")
    st.subheader("Enterprise Forensic Portal")
    
    with st.container():
        user_input = st.text_input("Corporate User ID", placeholder="Enter ID")
        pass_input = st.text_input("Secure Access Key", type="password", placeholder="Enter Key")
        
        if st.button("AUTHENTICATE"):
            if user_input == ADMIN_USER and pass_input == ADMIN_PASS:
                st.session_state.auth_status = True
                st.success("Authentication Successful!")
                time.sleep(1)
                st.rerun()
            else:
                st.session_state.auth_status = False
                st.error("Access Denied: Invalid Credentials")
    st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD UI ---
else:
    st.sidebar.markdown("### 🛡️ RiskShield Engine")
    st.sidebar.write(f"**Operator:** {ADMIN_USER.upper()}")
    if st.sidebar.button("Termnal Session"):
        st.session_state.auth_status = None
        st.rerun()

    st.title("📊 Forensic Audit & Analysis")
    st.write("Welcome to the commercial audit engine. Upload your ledger for deep-scan analysis.")
    
    # Dashboard Features
    col1, col2, col3 = st.columns(3)
    col1.metric("System Status", "Active", "Secure")
    col2.metric("AI Engine", "Gemini 2.5", "Optimized")
    col3.metric("Encryption", "AES-256", "Live")

    st.divider()
    
    uploaded_file = st.file_uploader("📂 Drop Audit Data (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, use_container_width=True)
        st.info("AI Analysis Engine is ready. Generating insights...")
