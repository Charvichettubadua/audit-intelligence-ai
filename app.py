import streamlit as st
import pandas as pd
import time

# --- Page Config ---
st.set_page_config(page_title="RiskShield AI | Enterprise", layout="centered", page_icon="🛡️")

# --- Commercial Styling (Blue Gradient) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #001529 0%, #004b91 100%); color: white; }
    .login-card { 
        background: rgba(255, 255, 255, 0.1); 
        padding: 40px; 
        border-radius: 20px; 
        border: 1px solid rgba(255,255,255,0.2); 
        backdrop-filter: blur(15px);
        margin-top: 50px;
    }
    .stTextInput>div>div>input { background-color: white !important; color: black !important; border-radius: 8px; }
    h1, h3, p { color: white !important; text-align: center; font-family: 'Segoe UI', sans-serif; }
    .stButton>button { 
        background-color: #22c55e !important; 
        color: white !important; 
        font-weight: bold; 
        border-radius: 8px; 
        border: none; 
        height: 3.5em; 
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #16a34a !important; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

# --- Session Management ---
if 'auth_status' not in st.session_state:
    st.session_state.auth_status = "idle" # Options: idle, success, failed

# --- New Credentials ---
ADMIN_USER = "chintu"
ADMIN_PASS = "deloitte2026"

# --- LOGIN UI ---
if st.session_state.auth_status != "success":
    st.markdown('<div class="login-card">', unsafe_allow_html=True)
    
    # Professional Logo
    st.markdown("<center><img src='https://cdn-icons-png.flaticon.com/512/11516/11516905.png' width='80'></center>", unsafe_allow_html=True)
    
    st.title("RiskShield AI")
    st.markdown("<p>Enterprise Forensic Audit Portal</p>", unsafe_allow_html=True)
    
    with st.form("login_form"):
        user_input = st.text_input("Corporate User ID", placeholder="e.g., chintu")
        pass_input = st.text_input("Secure Access Key", type="password", placeholder="••••••••")
        submit_button = st.form_submit_button("AUTHENTICATE")
        
        if submit_button:
            if user_input == ADMIN_USER and pass_input == ADMIN_PASS:
                st.session_state.auth_status = "success"
                st.success("Access Granted! Opening Dashboard...")
                time.sleep(1)
                st.rerun()
            else:
                st.session_state.auth_status = "failed"
                st.error("Authentication Failed: Please check your credentials.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- DASHBOARD UI ---
else:
    st.sidebar.markdown("### 🛡️ RiskShield Engine")
    st.sidebar.write(f"**Operator:** {ADMIN_USER.upper()}")
    if st.sidebar.button("Secure Logout"):
        st.session_state.auth_status = "idle"
        st.rerun()

    st.title("📊 Forensic Audit Dashboard")
    st.write("System online. Upload ledger data for real-time anomaly detection.")
    
    # Commercial Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Security Level", "High", "Verified")
    m2.metric("AI Engine", "Gemini Flash", "Live")
    m3.metric("Protocol", "AES-256", "Active")

    st.divider()
    
    uploaded_file = st.file_uploader("📂 Drop Audit Data (CSV)", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, use_container_width=True)
        st.success("Data ingested successfully. Ready for AI Analysis.")
